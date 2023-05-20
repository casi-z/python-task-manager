from PyQt6.QtWidgets import *
from components import *
from pages import *
from components import Redirect
from datetime import datetime
from calendar import monthrange, weekday


class Calendar(QWidget):

    def __init__(self):

        super().__init__()
       
        
        self.month = Month(datetime.now().month, datetime.now().year)
        self.days = self.month.get_days()
       

        


        
        print(self.days)
        
        main = AppLayout()
        day_item = AppLayout()
        day_array = []
        for day in self.days:
            
            day_item__number = AppLayout()
            day_item__name = AppLayout()
            
            day_item__number.render([
                QLabel(str(day.number))
            ])
            day_item__name.render([
                QLabel(day.name)
            ])
            day_array.append(
                day_item__number,
                
            )
            day_array.append(
                day_item__name,
                
            )

        day_item.render(day_array)

        main.render([day_item])

        self.setLayout(main)
