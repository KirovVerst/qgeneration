import datetime

from unittest import TestCase
from qgeneration.fields import DateField


class FieldsTest(TestCase):
    def test_date_field(self):
        start_date = datetime.date(year=1990, month=1, day=1)
        finish_date = datetime.date(year=2000, month=1, day=1)
        date_field = DateField('date_field', start_date, finish=finish_date)
        generated_date = date_field.generate()
        self.assertGreaterEqual(generated_date, start_date)
        self.assertLessEqual(generated_date, finish_date)
