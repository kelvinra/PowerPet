from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sqlite3

class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        loadUi('src/BuilderUI/Info.ui', self)
        self.stackedWidget.setCurrentIndex(0)

        # Menghubungkan tombol
        self.indtbtn = self.findChild(QPushButton, 'info')
        self.mafabtn = self.findChild(QPushButton, 'makanan')
        self.cakebtn = self.findChild(QPushButton, 'kesehatan')
        
        self.indtbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mafabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cakebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))


        def tampilin(self, id):
        # Menampilkan data umur
            conn = sqlite3.connect('src/DataBase/Hewan.db')
            cur = conn.cursor()
            cur.execute("SELECT umur FROM Hewan WHERE id=?", (id,))
            umur = cur.fetchone()[0]
            self.umur.setText(str(umur))

            # Menampilkan data lahir
            cur.execute("SELECT birthdate FROM Hewan WHERE id=?", (id,))
            lahir = cur.fetchone()[0]
            self.lahir.setText(str(lahir))

            # Menampilkan data gender
            cur.execute("SELECT jenis FROM Hewan WHERE id=?", (id,))
            gender = cur.fetchone()[0]
            self.gender.setText(str(gender))

            # Menampilkan data berat
            cur.execute("SELECT berat FROM Hewan WHERE id=?", (id,))
            berat = cur.fetchone()[0]
            self.berat.setText(str(berat))
