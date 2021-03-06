import datetime
from qgeneration.qfields import DateField, FirstNameQField
from qgeneration.qrecords import BaseRecord, PersonRecord

if __name__ == '__main__':
    start = datetime.date(year=1900, month=1, day=1)
    finish = datetime.date(year=2000, month=1, day=1)
    date_field = DateField('date_field', start, finish)

    first_name = FirstNameQField('first_name')
    record = BaseRecord(record_name='record', fields=[first_name, date_field])

    for _ in range(10):
        print(record.generate())

    person = PersonRecord('my_person')

    print(person.generate())
