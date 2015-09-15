from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
from accounts.models import IthacashUser
import csv
import StringIO
import copy
import sys
import mandrill
from base64 import b64encode
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        yesterday = datetime.now() - timedelta(days=1)

        most_recent_account_signups = IthacashUser.objects.filter(emails__created__gt=yesterday, accounts__created__gt=yesterday)

        if most_recent_account_signups:
            new_ithacash_users = []

            for user_object in most_recent_account_signups:

                # Get Emails child
                emails = user_object.emails.all()[0].__dict__

                # Get IthacashAccounts child
                accounts = user_object.accounts.all()[0].__dict__

                combined_user_dict = dict(emails, **accounts)
                combined_user_dict.update(user_object.__dict__)

                new_ithacash_users.append(combined_user_dict)

            csv_to_email = StringIO.StringIO()
            csv_writer = CyclosCsvWriter(new_ithacash_users, csv_to_email)
            csv_writer.map_dict_to_cyclos_fields(new_ithacash_users)
            csv_writer.output_to_csv(csv_to_email)

            mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

            try:
                result = mandrill_client.messages.send(
                    {
                        'to': [{'email': 'scott@ithacash.com'}],
                        'text': 'Import this CSV into Cyclos',
                        'from_name': 'Ithacash.com',
                        'from_email': "it@ithacash.com",
                        'subject': 'New user accounts',
                        'attachments': [
                            {
                                'type': 'text/csv',
                                'name': 'new_ithacash_users_%s' % datetime.now().strftime('%Y_%m_%d'),
                                'content': b64encode(csv_to_email.getvalue())
                            }
                        ]
                    })

                print "%s: %s" % (datetime.now(), result)

            except Exception, e:
                print "%s:  Error:\n%s" % (datetime.now(), e)

        else:
            print "%s: Nothing to send." % datetime.now()


class CyclosCsvWriter(object):

    cyclos_csv_to_ithacash_user_mapping = {
        'name': 'entity_name',
        'email': 'address',
        'username': 'username',
        'creationdate': 'created',
        'address[identifier].line1': 'address_1',
        'address[identifier].line2': 'address_2',
        'address[identifier].city': 'city',
        'address[identifier].region': 'state',
        'address[identifier].zip': 'zip_code',
        'mobile[identifier].number': 'phone_mobile',
        'landline[identifier].number': 'phone_landline'
    }

    cyclos_required_fieldnames = ('name', 'username', 'email', 'password', 'creationdate', 'broker', 'images', 'address[identifier].name', 'address[identifier].line1', 'address[identifier].line2', 'address[identifier].neighborhood', 'address[identifier].pobox', 'address[identifier].zip', 'address[identifier].city', 'address[identifier].region', 'address[identifier].country', 'address[identifier].private', 'mobile[identifier].name', 'mobile[identifier].number', 'mobile[identifier].private', 'landline[identifier].name', 'landline[identifier].number', 'landline[identifier].private')

    def __init__(self, new_ithacash_users, csv_output, *args, **kwargs):
        super(CyclosCsvWriter, self).__init__(*args, **kwargs)

        self.mapped = False
        self.cyclos_field_list = []
        self.new_ithacash_users = new_ithacash_users
        self.csv_output = csv_output

    def map_dict_to_cyclos_fields(self, new_ithacash_users=None):

        new_ithacash_users = new_ithacash_users or self.new_ithacash_users

        for new_user in new_ithacash_users:

            mapped_dict = dict.fromkeys(self.cyclos_required_fieldnames)

            for cyclos_field_name, ithacash_user_field_name in self.cyclos_csv_to_ithacash_user_mapping.iteritems():

                try:
                    new_value = new_user[ithacash_user_field_name]
                except KeyError:
                    raise TypeError("The dict didn't have a key '%s', which is required to map the data to a Cyclos CSV." % ithacash_user_field_name)

                mapped_dict[cyclos_field_name] = new_value

            mapped_dict['creationdate'] = mapped_dict['creationdate'].strftime('%m/%d/%Y')

            self.cyclos_field_list.append(mapped_dict)

        self.mapped = True

        return self.cyclos_field_list

    def output_to_csv(self, csv_ouput=None):

        if not self.mapped:
            raise AttributeError("You must run map_dict_to_cyclos_fields before you can write the CSV file.")

        csv_ouput = csv_ouput or self.csv_ouput

        writer = csv.DictWriter(csv_ouput, fieldnames=self.cyclos_required_fieldnames)

        writer.writeheader()

        for row in self.cyclos_field_list:
            writer.writerow(row)
