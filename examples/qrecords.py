import datetime
from qgeneration.qfields import DateQField, FirstNameQField
from qgeneration.qrecords import QRecord

if __name__ == '__main__':
    date_field = DateQField('date_field',
                            start=datetime.date(year=1990, month=1, day=1),
                            finish=datetime.date(year=2000, month=1, day=1))

    first_name = FirstNameQField('first_name')
    record = QRecord(name='record', fields=[first_name, date_field])
    for _ in range(10):
        print(record.generate())
