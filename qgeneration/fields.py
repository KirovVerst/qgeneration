import random
import datetime

FIRST_NAME_FIELD_TYPE = 0
LAST_NAME_FIELD_TYPE = 1
DATE_FIELD_TYPE = 2

DATASET = {
    FIRST_NAME_FIELD_TYPE: ['Arya', 'Jon', 'Sansa', 'Ned', 'Kate', 'Bran', 'Robb', 'Rickon', 'Jame'],
    LAST_NAME_FIELD_TYPE: ['Stark', 'Lannister', 'Baratheon', 'Targarien']
}


class BaseField:
    def __init__(self, name, field_type):
        self.name = name
        self.type = field_type


class CountryRelatedField(BaseField):
    def __init__(self, name, field_type, country):
        """
        Field that is depended on selected country
        :param name: str
        :param field_type: int
        :param country:
        """
        super(CountryRelatedField, self).__init__(name, field_type)
        self.country = country

    def generate(self):
        """
        Return random value from the dataset according a set type of field
        :return: str
        """
        return DATASET[self.type][random.randint(0, len(DATASET[self.type]) - 1)]


class FirstNameField(CountryRelatedField):
    def __init__(self, name, country=None):
        """

        :param name: str
        :param country:
        """
        self.country = country
        super(FirstNameField, self).__init__(name, FIRST_NAME_FIELD_TYPE, country)


class LastNameField(CountryRelatedField):
    def __init__(self, name, country=None):
        """

        :param name: str
        :param country:
        """
        super(LastNameField, self).__init__(name, LAST_NAME_FIELD_TYPE, country)


class DateField(BaseField):
    def __init__(self, name, start, finish):
        """

        :param name: str
        :param start: datetime.date
        :param finish: datetime.date
        """

        super(DateField, self).__init__(name, DATE_FIELD_TYPE)
        self.start_date = start
        self.finish_date = finish

    def generate(self):
        """
        Generate new date between `start_date` and `finish_date`, including both
        :return: datetime.date
        """
        delta = self.finish_date - self.start_date
        days = random.randint(0, delta.days)
        result_date = self.start_date + datetime.timedelta(days=days)
        return result_date
