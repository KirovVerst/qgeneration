import datetime
from unittest import TestCase

from qgeneration import qrecords, qfields


class QRecordsTestCase(TestCase):
    def test_qrecord(self):
        start = datetime.date(year=1990, month=1, day=1)
        finish = datetime.date(year=2000, month=1, day=1)
        date_field = qfields.DateQField('date_field', start=start, finish=finish)

        first_name = qfields.FirstNameQField('first_name')
        record = qrecords.QRecord(name='record', fields=[first_name, date_field])

        record_value = record.generate()

        self.assertIn(record_value[0], qfields.DATASET[qfields.FIRST_NAME_FIELD_TYPE])
        self.assertGreaterEqual(record_value[1], start)
        self.assertLessEqual(record_value[1], finish)
