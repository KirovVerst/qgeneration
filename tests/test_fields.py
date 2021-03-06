import datetime

from unittest import TestCase
from qgeneration import fields


class FieldsTest(TestCase):
    def test_date_field(self):
        start_date = datetime.date(year=1990, month=1, day=1)
        finish_date = datetime.date(year=2000, month=1, day=1)
        date_field = fields.DateField('date_field', start_date, finish=finish_date)
        generated_date = date_field.generate()
        self.assertGreaterEqual(generated_date, start_date)
        self.assertLessEqual(generated_date, finish_date)

    def test_first_name_field(self):
        first_name = fields.FirstNameField('first_name')
        self.assertIn(first_name.generate(), fields.DATASET[fields.FIRST_NAME_FIELD_TYPE])

    def test_last_name_field(self):
        first_name = fields.LastNameField('last_name')
        self.assertIn(first_name.generate(), fields.DATASET[fields.LAST_NAME_FIELD_TYPE])
