import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import MainWindow as mw
        




class app(QApplication):
    def __init__(self, argv):
        super(app, self).__init__(argv)
        self.window = mw.MainWindow()
        # self.menu = MenuWindow()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.window)
        self.widget.addWidget(self.menu)
        self.widget.setFixedWidth(1920)
        self.widget.setFixedHeight(1024)
        self.widget.show()
        self.window.Logo.clicked.connect(lambda: self.widget.setCurrentIndex(1))
    

        


run = app(sys.argv)

sys.exit(run.exec_())
