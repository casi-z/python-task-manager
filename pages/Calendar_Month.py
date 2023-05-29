from PyQt5 import QtCore, QtGui, QtWidgets
from components import *
from pages import *



class Calendar_Month():

    def __init__(self, window):
        self.window = window
        super().__init__()
       

        self.month_list = [
            {'color': 'blue', 'name': 'январь'},
            {'color': 'violet', 'name': 'февраль'},
            {'color': 'red', 'name': 'март'},
            {'color': 'green', 'name': 'апрель'},
            {'color': '#B2FF18', 'name': 'май'},
            {'color': 'yellow', 'name': 'июнь'},
            {'color': 'orange', 'name': 'июль'},
            {'color': 'red', 'name': 'август'},
            {'color': '#FF1833', 'name': 'сентябрь'},
            {'color': '#FF18B4', 'name': 'октябрь'},
            {'color': '#1888FF', 'name': 'ноябрь'},
            {'color': '#1842FF', 'name': 'декабрь'},
        ]
        

        window.setObjectName("MainWindow")
        window.resize(792, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        

        self.layout = QtWidgets.QHBoxLayout(self.tab)
        
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)
        

        for i in self.month_list:
            month_index = self.month_list.index(i)
            
            button = QtWidgets.QPushButton(f"{i['name']}")
            font = QtGui.QFont()
            font.setFamily("Georgia")
            font.setPointSize(12)
            button.setMinimumSize(60, 40)
            button.setFont(font)
            button.setStyleSheet("QPushButton{\n"
    "    border-radius:20px;\n"
    f"    background-color:{i['color']};\n"
    "}\n"
    "\n"
    "QPushButton:hover{\n"
    "    background-color:rgb(44, 90, 255);\n"
    "}")
            button.setObjectName(f"month_button_{i}")
            
            self.layout.addWidget(button)

            

            button.clicked.connect(lambda ch, btn=button :self.month_handle_click(btn))
            
                
    def month_handle_click(self, b):
        self.window.redirect("Calendar_Days(self)")

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Календарь"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Список задач"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Отчет"))




        # self.month = Month(datetime.now().month, datetime.now().year)
        # self.days = self.month.get_days()
       
        
        # main = AppLayout()
        
        # day_array = []
        
        # for day in self.days:
        #     day_item = AppLayout()
        #     day_item__number = AppLayout()
        #     day_item__name = AppLayout()
            
        #     day_item__number.render([
        #         QLabel(str(day.number))
        #     ])
        #     day_item__name.render([
        #         QLabel(day.name)
        #     ])
        #     day_item.renderLayout([
        #         day_item__number,
        #         day_item__name
        #     ])
            
        #     main.renderLayout([day_item])
        

        # self.setLayout(main)
