import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import MainWindow as mw
import MenuWindow as mw2
import Add as a
import klinik as k
import Info 
        


class app(QApplication):
    def __init__(self, argv):
        super(app, self).__init__(argv)
        self.window = mw.MainWindow()
        self.menu = mw2.MenuWindow()
        self.menu.createCard()
        self.add = a.AddWindow()
        self.klinik = k.klinikWindow()
        self.info = Info.InfoWindow()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.window)
        self.widget.addWidget(self.menu)
        self.widget.addWidget(self.add)
        self.widget.addWidget(self.klinik)
        self.widget.addWidget(self.info)
        self.widget.setFixedWidth(1920)
        self.widget.setFixedHeight(1024)
        self.widget.show()
        #buttons function
        self.window.Logo.clicked.connect(lambda: self.widget.setCurrentIndex(1))
        self.menu.Add.clicked.connect(lambda: self.widget.setCurrentIndex(2))
        self.add.submitbtn.clicked.connect(lambda: self.widget.setCurrentIndex(1))
        self.add.backHome.clicked.connect(lambda: self.widget.setCurrentIndex(1))
        self.menu.pushButton.clicked.connect(lambda: self.widget.setCurrentIndex(3))
        for i in range (0, len(self.menu.buttons)):
            self.menu.buttons[i].clicked.connect(partial(self.showDetail, i))
        
        
    def showDetail(self, i):
        self.widget.setCurrentIndex(4)
        self.info

        
    


run = app(sys.argv)

sys.exit(run.exec_())