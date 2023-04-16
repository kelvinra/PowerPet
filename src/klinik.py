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
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 500)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 150)
        
        self.load_data()
        searchBar = self.findChild(QLineEdit, 'searchBar_2')
        searchBar.textChanged.connect(lambda: self.search_data(searchBar.text().lower()))

    def load_data(self):
        conn = sqlite3.connect('src/DataBase/Hewan.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Klinik")
        data = cur.fetchall()

        # set jumlah kolom dan baris tableWidget
        self.tableWidget.setColumnCount(len(data[0])-1) # kurangi 1 untuk menghilangkan kolom IDKlinik
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(['Nama Klinik', 'Alamat', 'Jam Praktek', 'Kontak'])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # tampilkan data ke dalam tableWidget
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data[1:]): # mulai dari indeks ke-1 untuk menghilangkan kolom IDKlinik
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
                
    def search_data(self, search_term):
        print("Search term:", search_term)
        conn = sqlite3.connect('src/DataBase/Hewan.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM klinik WHERE LOWER(NamaKlinik) LIKE ? OR LOWER(Alamat) LIKE ? OR LOWER(Telepon) LIKE ?",
                    ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        data = cur.fetchall()
        self.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data[1:]):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

