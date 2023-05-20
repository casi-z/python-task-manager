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
        self.month = month
        self.year = year
        self.name = self.days_in_week[weekday(year, month, self.number)]
        self.weekend = self.is_weekend()
        self.today = self.is_today()
        
        self.month_name = self.month_list[month - 1]
        self.date = f'{self.number}.{month}.{year}'
        
        
    def is_today(self):
        print(self.month)
        if datetime.now().day == self.number and datetime.now().month == self.month and self.year == datetime.now().year:
            return True
        return False
    
    def is_weekend(self):
        if self.name == 'суббота' or self.name == 'воскресенье':
            return True
        return False
        

class Month:

    def __init__(self, number, year):
        self.number = number
        self.year = year

        

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

    def get_days(self):
        days_in_month = monthrange(self.year, self.number)[1]
        self.days = []

        for id in range(days_in_month):

            new_day = Day(id, self.number, self.year)
            self.days.append(new_day)
            # self.days.append({
            #     'number': new_day.number,
            #     'name': new_day.name,
            #     'year': new_day.year,
            #     'month': new_day.month,
            #     'weekend': new_day.weekend,
            #     'date': new_day.date,
            #     'today': new_day.today,
            #     'month_name': new_day.month_name,
                
            # })


        return self.days

