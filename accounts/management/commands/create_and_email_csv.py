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

    def __init__(self, new_user_list=None, *args, **kwargs):

        super(Command, self).__init__(*args, **kwargs)

        self.new_ithacash_users = new_user_list or []
        self.cyclos_field_list = []
        self.csv_buffer = StringIO.StringIO()
        self.mapped_dict = dict.fromkeys(self.cyclos_required_fieldnames)
        self.csv_output = csv.DictWriter(self.csv_buffer, fieldnames=self.cyclos_required_fieldnames)

    def add_arguments(self, parser):
        parser.add_argument('--user', action='append', help='Specify multiple users with additional --user arguments')

    def handle(self, *args, **options):

        if self.get_most_recent_signups(options):
            self.map_cyclos_keys_to_ithacash_user_values(self.new_ithacash_users)
            self.output_csv()
            print self.email_csv(self.csv_buffer)

        else:
            print "%s: Nothing to send." % datetime.now()

    def get_most_recent_signups(self, options):

        yesterday = datetime.now() - timedelta(days=1)

        if options['user']:
            most_recent_account_signups = []
            for user in options['user']:
                print user
                user_object = IthacashUser.objects.get(username=user)
                most_recent_account_signups.append(user_object)
        else:
            yesterday = datetime.now() - timedelta(days=1)

            most_recent_account_signups = IthacashUser.objects.filter(emails__created__gt=yesterday, accounts__created__gt=yesterday)

        if most_recent_account_signups:

            for user_object in most_recent_account_signups:

                # Get Emails child
                emails = user_object.emails.all()[0].__dict__

                # Get IthacashAccounts child
                accounts = user_object.accounts.all()[0].__dict__

                combined_user_dict = dict(emails, **accounts)
                combined_user_dict.update(user_object.__dict__)

                self.new_ithacash_users.append(combined_user_dict)

        return self.new_ithacash_users

    def map_cyclos_keys_to_ithacash_user_values(self, new_ithacash_users=None):

        new_ithacash_users = new_ithacash_users or self.new_ithacash_users

        for new_user in new_ithacash_users:

            if new_user['account_type'] != 'Individual' and new_user['entity_name'] == '':
                new_user['entity_name'] = new_user['full_name']
                print new_user['entity_name']

            mapped_dict = dict.fromkeys(self.cyclos_required_fieldnames)

            for cyclos_field_name, ithacash_user_field_name in self.cyclos_csv_to_ithacash_user_mapping.iteritems():

                try:
                    new_value = new_user[ithacash_user_field_name]
                except KeyError:
                    raise TypeError("The dict didn't have a key '%s', which is required to map the data to a Cyclos CSV." % ithacash_user_field_name)

                mapped_dict[cyclos_field_name] = new_value

            mapped_dict['creationdate'] = mapped_dict['creationdate'].strftime('%m/%d/%Y')

            # Cyclos chokes on equivalent mobile and landline numbers,
            # so blank the landline if that's true
            if mapped_dict['landline[identifier].number'] and mapped_dict['landline[identifier].number'] == mapped_dict['mobile[identifier].number']:
                mapped_dict['landline[identifier].number'] = ''

            self.cyclos_field_list.append(mapped_dict)

        self.mapped = True

        return self.cyclos_field_list

    def output_csv(self, csv_buffer=None):

        if not self.mapped:
            raise AttributeError("You must run map_cyclos_keys_to_ithacash_user_values before you can write the CSV file.")

        csv_buffer = csv_buffer or self.csv_buffer

        self.csv_output.writeheader()

        for row in self.cyclos_field_list:
            self.csv_output.writerow(row)

        return self.csv_buffer

    def email_csv(self, csv_buffer=None):

        csv_buffer = csv_buffer or self.csv_buffer

        try:
            mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)

            result = mandrill_client.messages.send(
                {
                    'to': [{'email': 'shane@ithacash.com'}],
                    'text': 'Import this CSV into Cyclos',
                    'from_name': 'Ithacash.com',
                    'from_email': "it@ithacash.com",
                    'subject': 'New user accounts',
                    'attachments': [
                        {
                            'type': 'text/csv',
                            'name': 'new_ithacash_users_2015_08_30',
                            'content': b64encode(csv_buffer.getvalue())
                        }
                    ]
                })

            return "%s: %s" % (datetime.now(), result)

        except Exception, e:
            return "%s:  Error:\n%s" % (datetime.now(), e)
