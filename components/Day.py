from calendar import monthrange, weekday
from datetime import datetime

class Day:

    def __init__(self, number, month, year):

        self.month_list = [
            'январь',
            'февраль',
            'март',
            'апрель',
            'май',
            'июнь',
            'июль',
            'август',
            'сентябрь',
            'октябрь',
            'ноябрь',
            'декабрь',
        ]

        self.days_in_week = [
            'понедельник',
            'вторник',
            'среда',
            'четверг',
            'пятница',
            'суббота',
            'воскресенье',
        ]

        self.number = number + 1
        self.name = self.days_in_week[weekday(year, month, self.number)]
        self.weekend = self.__is_weekend()
        self.today = self.__is_today()
        self.month = month
        self.month_name = self.month_list[month - 1]
        self.date = f'{self.number}.{month}.{year}'
        self.year = year

    def __is_today(self):
        # print(datetime.now().day, datetime.now().month, datetime.now().year)
        if datetime.now().day == self.number and datetime.now().month == self.month and self.year == datetime.now().year:
            return True
        return False
    
    def __is_weekend(self):
        if self.name == 'суббота' or self.name == 'воскресенье':
            return True
        return False
        