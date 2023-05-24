from PyQt5 import QtCore, QtGui, QtWidgets
from components import *
from pages import *



class Calendar():

    def __init__(self, window):

        super().__init__()
       
        window.setObjectName("MainWindow")
        window.resize(792, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.month_button = QtWidgets.QPushButton(self.tab)
        self.month_button.setGeometry(QtCore.QRect(40, 30, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.month_button.setFont(font)
        self.month_button.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background-color:#476DD5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(44, 90, 255);\n"
"}")
        self.month_button.setObjectName("month_button")

        self.month_button_2 = QtWidgets.QPushButton(self.tab)
        self.month_button_2.setGeometry(QtCore.QRect(140, 30, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.month_button_2.setFont(font)
        self.month_button_2.setStyleSheet("QPushButton{\n"
"    border-radius:20px;\n"
"    background-color:#476DD5;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(44, 90, 255);\n"
"}")
        self.month_button_2.setObjectName("month_button_2")

        for i in range(12):

            eval(f"""self.month_button{i} = QtWidgets.QPushButton(self.tab)\nself.month_button{str(i)}.setGeometry(QtCore.QRect(240, 30, 81, 71))\nfont = QtGui.QFont()\nfont.setFamily("Georgia")\nfont.setPointSize(12)\nself.month_button{str(i)}.setFont(font)\nself.month_button{str(i)}.setObjectName("month_button{str(i)}")\nself.month_button{str(i)}.setText("ЯНВАРЬ")""".replace('|', '{').replace('||', '}'))
        
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
        
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.month_button.setText(_translate("MainWindow", "ЯНВАРЬ"))
        self.month_button_2.setText(_translate("MainWindow", "ЯНВАРЬ"))
        
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
