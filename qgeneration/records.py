import datetime
from qgeneration.fields import FirstNameField, LastNameField, DateField


class BaseRecord:
    def __init__(self, record_name, fields):
        self.record_name = record_name
        self.fields = fields
        self.id = 0

    def generate(self):
        self.id += 1
        return [self.id] + [field.generate() for field in self.fields]


class PersonRecord(BaseRecord):
    def __init__(self, record_name, start_date=None, finish_date=None):
        if start_date is None:
            start_date = datetime.date(year=1990, month=1, day=1)
        if finish_date is None:
            finish_date = datetime.date(year=2000, month=1, day=1)
        fields = [FirstNameField('first_name'),
                  LastNameField('last_name'),
                  DateField('birthday', start_date, finish_date)]
        super(PersonRecord, self).__init__(record_name, fields)
