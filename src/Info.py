from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        loadUi('src/BuilderUI/Info.ui', self)
        self.indtbtn= self.findChild(QPushButton, 'indt')
        self.mafabtn= self.findChild(QPushButton, 'mafa')
        self.cakebtn= self.findChild(QPushButton, 'cake')

        self.indtbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mafabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cakebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
    





