import datetime
from unittest import TestCase

from qgeneration import records, fields


class QRecordsTestCase(TestCase):
    def test_qrecord(self):
        start = datetime.date(year=1990, month=1, day=1)
        finish = datetime.date(year=2000, month=1, day=1)
        date_field = fields.DateField('date_field', start=start, finish=finish)

        first_name = fields.FirstNameField('first_name')
        record = records.BaseRecord(record_name='record', fields=[first_name, date_field])

        record_value = record.generate()

        self.assertIn(record_value[1], fields.DATASET[fields.FIRST_NAME_FIELD_TYPE])
        self.assertGreaterEqual(record_value[2], start)
        self.assertLessEqual(record_value[2], finish)

    def test_person_record(self):
        person = records.PersonRecord('my_person')
        data = person.generate()
        self.assertEqual(len(data), 4)
        self.assertEqual(data[0], 1)
