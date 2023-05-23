from PyQt5 import QtCore, QtGui, QtWidgets
from components import *
from pages import *



class Calendar():

    def __init__(self, window):

        super().__init__()
       
        window.setObjectName("MainWindow")
        window.resize(930, 559)
        window.setStyleSheet("background: white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 931, 511))
        self.tabWidget.setStyleSheet("background: white;\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.calendar_tab = QtWidgets.QWidget()
        self.calendar_tab.setObjectName("calendar_tab")
        self.week = QtWidgets.QGroupBox(self.calendar_tab)
        self.week.setGeometry(QtCore.QRect(0, -10, 931, 81))
        self.week.setStyleSheet("background: none")
        self.week.setObjectName("week")
        self.day_item = QtWidgets.QPushButton(self.week)
        self.day_item.setGeometry(QtCore.QRect(0, 10, 81, 71))
        self.day_item.setStyleSheet("background: none;")
        self.day_item.setText("")
        self.day_item.setObjectName("day_item")
        self.day_number = QtWidgets.QLabel(self.week)
        self.day_number.setGeometry(QtCore.QRect(30, 30, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.day_number.setFont(font)
        self.day_number.setStyleSheet("")
        self.day_number.setObjectName("day_number")
        self.day_name = QtWidgets.QLabel(self.week)
        self.day_name.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.day_name.setObjectName("day_name")
        self.tabWidget.addTab(self.calendar_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calendar_tab.setToolTip(_translate("MainWindow", "<html><head/><body><p>Календарь</p></body></html>"))
        self.week.setTitle(_translate("MainWindow", "GroupBox"))
        self.day_number.setText(_translate("MainWindow", "1"))
        self.day_name.setText(_translate("MainWindow", "Понедельник"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calendar_tab), _translate("MainWindow", "Календарь"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Список дел"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Отчёты"))




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
