from PyQt5 import QtCore, QtGui, QtWidgets

class Calendar_Days():

    def __init__(self, window):
        self.window = window
        super().__init__()
        window.setObjectName("Form")
        window.resize(508, 484)
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(210, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(window)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(window)
        self.label_3.setGeometry(QtCore.QRect(120, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(window)
        self.label_4.setGeometry(QtCore.QRect(180, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(window)
        self.label_5.setGeometry(QtCore.QRect(240, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(window)
        self.label_6.setGeometry(QtCore.QRect(300, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(window)
        self.label_7.setGeometry(QtCore.QRect(360, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(window)
        self.label_8.setGeometry(QtCore.QRect(420, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_7 = QtWidgets.QPushButton(window)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 130, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    border-radius:8px;\n"
"    background-color:#347cc4\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#6c94dc\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ЯНВАРЬ"))
        self.label_2.setText(_translate("Form", "ПН"))
        self.label_3.setText(_translate("Form", "ВТ"))
        self.label_4.setText(_translate("Form", "СР"))
        self.label_5.setText(_translate("Form", "ЧТ"))
        self.label_6.setText(_translate("Form", "ПТ"))
        self.label_7.setText(_translate("Form", "СБ"))
        self.label_8.setText(_translate("Form", "ВС"))
        self.pushButton_7.setText(_translate("Form", "1"))
