from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/BuilderUI/Main.ui', self)
