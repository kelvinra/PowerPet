import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import Button as btn
import sqlite3

class klinikWindow(QDialog):
    def __init__(self):
        super(klinikWindow, self).__init__()
        loadUi('src/BuilderUI/klinik.ui', self)
        self.satubtn = self.findChild(QPushButton, 'satu')
        self.tableWidget.setColumnWidth(0, 500)
        self.tableWidget.setColumnWidth(1, 600)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(3, 400)

        self.load_data()

    def load_data(self):
        conn = sqlite3.connect('src/DataBase/Hewan.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Klinik")
        data = cur.fetchall()

        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(['ID Klinik', 'Nama Klinik', 'Alamat', 'Jam Praktek', 'Telepon'])

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
