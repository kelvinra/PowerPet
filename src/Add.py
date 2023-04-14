from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class AddWindow(QDialog):
    def __init__(self):
        super(AddWindow, self).__init__()
        loadUi('src/BuilderUI/Add.ui', self)
        self.satubtn= self.findChild(QPushButton, 'satu')
        self.duabtn= self.findChild(QPushButton, 'dua')
        self.tigabtn= self.findChild(QPushButton, 'tiga')
        self.stackedWidget.setCurrentIndex(0)
        # Connect the button's clicked signal to a slot that switches to page 1
        self.satubtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.duabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.tigabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))