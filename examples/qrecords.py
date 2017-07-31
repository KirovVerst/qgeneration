import datetime
from qgeneration.qfields import DateQField, FirstNameQField
from qgeneration.qrecords import QRecord, PersonQRecord

if __name__ == '__main__':
    start = datetime.date(year=1900, month=1, day=1)
    finish = datetime.date(year=2000, month=1, day=1)
    date_field = DateQField('date_field', start, finish)

    first_name = FirstNameQField('first_name')
    record = QRecord(record_name='record', fields=[first_name, date_field])

    for _ in range(10):
        print(record.generate())

    person = PersonQRecord('my_person')

    print(person.generate())
