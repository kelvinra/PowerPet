import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import MainWindow as mw
import MenuWindow as mw2
import Add as a
import JadwalWindow as jw




class app(QApplication):
    def __init__(self, argv):
        super(app, self).__init__(argv)
        self.window = mw.MainWindow()
        self.menu = mw2.MenuWindow()
        self.add = a.AddWindow()
        self.jadwal = jw.JadwalWindow()
        self.widget = QtWidgets.QStackedWidget()
        # self.widget.addWidget(self.window)
        # self.widget.addWidget(self.menu)
        # self.widget.addWidget(self.add)
        self.widget.addWidget(self.jadwal)
        self.widget.setFixedWidth(1920)
        self.widget.setFixedHeight(1024)
        self.widget.show()
        # self.window.Logo.clicked.connect(lambda: self.widget.setCurrentIndex(1))
        # self.menu.Add.clicked.connect(lambda: self.widget.setCurrentIndex(2))
        # self.add.submitbtn.clicked.connect(lambda: self.widget.setCurrentIndex(1))
        # self.add.backHome.clicked.connect(lambda: self.widget.setCurrentIndex(1))
    



run = app(sys.argv)

sys.exit(run.exec_())
