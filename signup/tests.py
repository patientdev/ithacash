from django.test import TestCase
from signup.factories import SignupFactory
from signup.utils import CyclosCsvWriter, CYCLOS_CSV_USER_SIGNUP_MODEL_MAPPING


class CSVTests(TestCase):

    def test_map_data_from_dict(self):

        signup_object = SignupFactory()

        writer = CyclosCsvWriter(
                        signup_object=signup_object,
                        csvfile_path='/nowhere/'
        )

        mapped_dict = writer.map_dict_to_cyclos_fields()

        for k, v in CYCLOS_CSV_USER_SIGNUP_MODEL_MAPPING.items():
            object_value = getattr(signup_object, v)
            mapped_dict_value = mapped_dict[k]
            self.assertEqual(object_value, mapped_dict_value)

