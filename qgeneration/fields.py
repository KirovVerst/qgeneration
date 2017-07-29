import random
import datetime

FIRST_NAME_FIELD_TYPE = 0
LAST_NAME_FIELD_TYPE = 1
DATE_FIELD_TYPE = 2

DATA = {
    FIRST_NAME_FIELD_TYPE: ['Arya', 'Jon', 'Sansa', 'Ned', 'Kate', 'Bran', 'Robb', 'Rickon', 'Jame'],
    LAST_NAME_FIELD_TYPE: ['Stark', 'Lanister', 'Baratheon', 'Targarien']
}


class BaseField:
    def __init__(self, name, field_type):
        self.name = name
        self.type = field_type


class CountryRelatedField(BaseField):
    def __init__(self, name, field_type, country):
        super(CountryRelatedField, self).__init__(name, field_type)
        self.country = country

    def generate(self):
        return DATA[self.type][random.randint(0, len(DATA[self.type]))]


class FirstNameField(CountryRelatedField):
    def __init__(self, name, country):
        self.country = country
        super(FirstNameField, self).__init__(name, FIRST_NAME_FIELD_TYPE, country)


class LastNameField(CountryRelatedField):
    def __init__(self, name, country):
        super(LastNameField, self).__init__(name, LAST_NAME_FIELD_TYPE, country)


class DateField(BaseField):
    def __init__(self, name, start, finish):
        super(DateField, self).__init__(name, DATE_FIELD_TYPE)
        self.start = start
        self.finish = finish

    def generate(self):
        delta = self.finish - self.start
        days = random.randint(0, delta.days)
        result_date = self.start + datetime.datetime(year=0, month=0, day=days)
        return result_date
