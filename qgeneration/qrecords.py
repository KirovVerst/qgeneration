import datetime
from qgeneration.qfields import FirstNameQField, LastNameQField, DateQField


class QRecord:
    def __init__(self, record_name, fields):
        self.record_name = record_name
        self.fields = fields
        self.id = 0

    def generate(self):
        self.id += 1
        return [self.id] + [field.generate() for field in self.fields]


class PersonQRecord(QRecord):
    def __init__(self, record_name, start_date=None, finish_date=None):
        if start_date is None:
            start_date = datetime.date(year=1990, month=1, day=1)
        if finish_date is None:
            finish_date = datetime.date(year=2000, month=1, day=1)
        fields = [FirstNameQField('first_name'),
                  LastNameQField('last_name'),
                  DateQField('birthday', start_date, finish_date)]
        super(PersonQRecord, self).__init__(record_name, fields)
