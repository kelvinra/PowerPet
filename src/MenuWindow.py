import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class MenuWindow(QDialog):
    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi('src\BuilderUI\Menu.ui', self)
        self.Arrow.clicked.connect(self.slideright)
        self.Arrow_2.clicked.connect(self.slideleft)
        self.poscarosel = 0
    
    def slideleft(self):
        self.animation = QPropertyAnimation(self.carousel, b"pos")
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(self.poscarosel, 250))
        self.poscarosel += 480
        self.animation.setEndValue(QPoint(self.poscarosel,250))
        self.animation.setDuration(500)
        self.animation.start()
    
    def slideright(self):
        self.animation = QPropertyAnimation(self.carousel, b"pos") 
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(self.poscarosel, 250))
        self.poscarosel -= 480
        self.animation.setEndValue(QPoint(self.poscarosel,250))
        self.animation.setDuration(500)
        self.animation.start()