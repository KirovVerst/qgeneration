import datetime
from qgeneration.fields import DateField, FirstNameField

if __name__ == '__main__':
    date_field = DateField('date_field',
                           start=datetime.date(year=1990, month=1, day=1),
                           finish=datetime.date(year=2000, month=1, day=1))
    date = date_field.generate()

    first_name = FirstNameField('first_name')
    for _ in range(5):
        print(first_name.generate())
