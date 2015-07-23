import __builtin__

from django.test import TestCase
from mock.mock import patch, mock_open
from signup.factories import SignupFactory
from signup.utils import CyclosCsvWriter, CYCLOS_CSV_USER_SIGNUP_MODEL_MAPPING


class CSVTests(TestCase):

    def setUp(self):
        self.signup_object = SignupFactory()

    def test_map_data_from_dict(self):

        writer = CyclosCsvWriter(
                        signup_object=self.signup_object,
                        csvfile_path='/nowhere/'
        )

        mapped_dict = writer.map_dict_to_cyclos_fields()

        for k, v in CYCLOS_CSV_USER_SIGNUP_MODEL_MAPPING.items():
            object_value = getattr(self.signup_object, v)
            mapped_dict_value = mapped_dict[k]
            self.assertEqual(object_value, mapped_dict_value)

    def test_write_csv(self):

        writer = CyclosCsvWriter(
                        signup_object=self.signup_object,
                        csvfile_path='/nowhere/'
        )

        writer.map_dict_to_cyclos_fields()

        with patch.object(__builtin__, 'open', mock_open()) as mock_writer:
            writer.write_csv()
            mock_writer.assert_called_once_with('/nowhere/', 'a')
