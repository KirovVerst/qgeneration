import datetime
from qgeneration.fields import DateField

if __name__ == '__main__':
    date_field = DateField('date_field',
                           start=datetime.date(year=1990, month=1, day=1),
                           finish=datetime.date(year=2000, month=1, day=1))
    for _ in range(10):
        print(date_field.generate())
