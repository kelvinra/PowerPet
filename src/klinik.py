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
        self.max_table_height = self.tableWidget.height() # simpan tinggi maksimum sebelum pencarian
        searchBar = self.findChild(QLineEdit, 'searchBar_2')
        self.backHome.clicked.connect(lambda: self.close())
        searchBar.textChanged.connect(lambda: self.search_data(searchBar.text().lower()))

    def load_data(self):
        conn = sqlite3.connect('src/DataBase/Hewan.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Klinik")
        data = cur.fetchall()

        self.tableWidget.setColumnCount(len(data[0])-1)
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(['Nama Klinik', 'Alamat', 'Jam Praktek', 'Kontak'])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data[1:]):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row_num, col_num, item)
    def search_data(self, search_term):
        conn = sqlite3.connect('src/DataBase/Hewan.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM klinik WHERE LOWER(NamaKlinik) LIKE ? OR LOWER(Alamat) LIKE ? OR LOWER(Telepon) LIKE ?",
                    ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        data = cur.fetchall()

        self.tableWidget.setRowCount(len(data))

        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 500)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setVerticalHeaderLabels([str(i+1) for i in range(len(data))]) # tambahkan baris ini untuk menambahkan label baris

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data[1:]):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row_num, col_num, item)
                
        # Atur rata tengah untuk header vertikal
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem(str(i+1)))
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem(str(i+1)))
            self.tableWidget.verticalHeaderItem(i).setTextAlignment(Qt.AlignCenter)
            
        # Batasi ketinggian tabel agar tidak melebihi tinggi maksimum sebelum pencarian
        table_height = self.tableWidget.horizontalHeader().height()
        for row in range(self.tableWidget.rowCount()):
            table_height += self.tableWidget.rowHeight(row)
        self.tableWidget.setFixedHeight(min(table_height, self.max_table_height))
