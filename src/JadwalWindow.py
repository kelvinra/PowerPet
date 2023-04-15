from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class JadwalWindow(QDialog):
    def __init__(self):
        super(JadwalWindow, self).__init__()
        loadUi('src/BuilderUI/Jadwal.ui', self)