from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget
import sys
 
 
class Calendar():
    def __init__(self):
        self.widget = QWidget(self)
        
        self.calendar = QCalendarWidget(self.widget)
        self.setCentralWidget(self.widget)
        