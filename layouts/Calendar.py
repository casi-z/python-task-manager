from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Calendar(QWidget):
    def __init__(self, Form):
        super().__init__()
        
        Form.setObjectName("Form")
        Form.resize(792, 600)
        self.calendar = QtWidgets.QCalendarWidget(Form)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 792, 600))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.calendar.setFont(font)
        self.calendar.setObjectName("calendar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))