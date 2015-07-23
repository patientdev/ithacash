import os
import csv
from datetime import datetime
from django.conf import settings

CYCLOS_FIELDNAMES = ('name', 'username', 'email', 'password', 'creationdate', 'broker', 'images',
                         'address[identifier].name', 'address[identifier].line1', 'address[identifier].line2',
                         'address[identifier].neighborhood', 'address[identifier].pobox', 'address[identifier].zip',
                         'address[identifier].city', 'address[identifier].region', 'address[identifier].country',
                         'address[identifier].private', 'mobile[identifier].name', 'mobile[identifier].number',
                         'mobile[identifier].private', 'landline[identifier].name', 'landline[identifier].number',
                         'landline[identifier].private')

CYCLOS_CSV_USER_SIGNUP_MODEL_MAPPING = {  # Move this to a more sane place, perhaps to the model.
    'name':                        'name_business',
    'email':                       'email',  # Do we need this?
    'username':                    'name_login',
    'creationdate':                'created',
    'address[identifier].line1':   'address_1',
    'address[identifier].line2':   'address_2',
    'address[identifier].city':    'address_city',
    'address[identifier].region':  'address_state',
    'address[identifier].zip':     'address_zip_code',
    'mobile[identifier].number':   'phone_mobile',
    'landline[identifier].number': 'phone_landline'
}


class CyclosCsvWriter(object):
    '''
    Writes a CSV file, mapped to cyclos taxonomy.
    '''

    def __init__(self, signup_object, csvfile_path, *args, **kwargs):
        super(CyclosCsvWriter, self).__init__(*args, **kwargs)

        self.mapped = False
        self.cyclos_field_dict = dict.fromkeys(CYCLOS_FIELDNAMES)
        self.form_input_dict = signup_object.__dict__
        self.csvfile_path = csvfile_path

    def map_dict_to_cyclos_fields(self, form_dict=None):
        '''
        Iterate through all field names needed for proper Cyclos CSV,
        get corresponding values from self.form_input_dict,
        use them to populate self.cyclos_field_dict
        '''
        form_dict = form_dict or self.form_input_dict

        for cyclos_field_name, form_field_name in CYCLOS_CSV_USER_SIGNUP_MODEL_MAPPING.iteritems():

            try:
                new_value = form_dict[form_field_name]
            except KeyError:
                raise TypeError("The form didn't have a key '%s', which is required to map the data to a Cyclos CSV." % form_field_name)
            self.cyclos_field_dict[cyclos_field_name] = new_value

        self.mapped = True

        return self.cyclos_field_dict

    def write_csv(self, csvfile_path=None):

        if not self.mapped:
            raise AttributeError("You must run map_dict_to_cyclos_fields before you can write the CSV file.")

        csvfile_path = csvfile_path or self.csvfile_path

        with open(csvfile_path, 'a+') as f:
            writer = csv.DictWriter(f, fieldnames=CYCLOS_FIELDNAMES)

            if not os.path.isfile(csvfile_path):
                writer.writeheader()

            writer.writerow(self.cyclos_field_dict)
