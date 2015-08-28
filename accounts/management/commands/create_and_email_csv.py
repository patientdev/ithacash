from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
from accounts.models import IthacashUser
from accounts.utils import CyclosCsvWriter
import csv
import StringIO
import copy


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        since_yesterday_morning = datetime.now() - timedelta(days=1)

        most_recent_account_signups = IthacashUser.objects.filter(emails__created__gt=since_yesterday_morning, accounts__created__gt=since_yesterday_morning)

        for new_user in most_recent_account_signups:

            emails = new_user.emails.all()[0].__dict__
            accounts = new_user.accounts.all()[0].__dict__

            new_user_dict = new_user.__dict__

            new_user_dict.update(emails)
            new_user_dict.update(accounts)

            csv_to_email = StringIO.StringIO()
            csv_writer = CyclosCsvWriter(new_user, csv_to_email)
            csv_writer.map_dict_to_cyclos_fields(new_user)
            csv_writer.write_csv(csv_to_email)

            print csv_to_email.getvalue()


