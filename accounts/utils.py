import os
import csv
import base64
import sys
import mandrill
from accounts.models import IthacashUser

class CyclosCsvWriter(object):

    cyclos_csv_to_ithacash_user_mapping = {
        'name': 'entity_name',
        'email': 'address',  # Do we need this?
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

    def __init__(self, ithacash_user_object, csvfile_path, *args, **kwargs):
        super(CyclosCsvWriter, self).__init__(*args, **kwargs)

        self.mapped = False
        self.cyclos_field_dict = dict.fromkeys(self.cyclos_required_fieldnames)
        self.ithacash_user_dict = ithacash_user_object.__dict__
        self.csvfile_path = csvfile_path

    def map_dict_to_cyclos_fields(self, ithacash_user_dict=None):
        '''
        Iterate through all field names needed for proper Cyclos CSV,
        get corresponding values from self.form_input_dict,
        use them to populate self.cyclos_field_dict
        '''
        ithacash_user_dict = ithacash_user_dict.__dict__ or self.ithacash_user_dict.__dict__

        for cyclos_field_name, ithacash_user_field_name in self.cyclos_csv_to_ithacash_user_mapping.iteritems():

            try:
                new_value = ithacash_user_dict[ithacash_user_field_name]
            except KeyError:
                raise TypeError("The dict didn't have a key '%s', which is required to map the data to a Cyclos CSV." % ithacash_user_field_name)
            self.cyclos_field_dict[cyclos_field_name] = new_value

        self.mapped = True

        return self.cyclos_field_dict

    def write_csv(self, csvfile_path=None):

        if not self.mapped:
            raise AttributeError("You must run map_dict_to_cyclos_fields before you can write the CSV file.")

        csvfile_path = csvfile_path or self.csvfile_path

        writer = csv.DictWriter(csvfile_path, fieldnames=self.cyclos_required_fieldnames)

        writer.writeheader()

        writer.writerow(self.cyclos_field_dict)
