import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import Button as btn
import sqlite3 as mdb

class AddWindow(QDialog):
    def __init__(self):
        super(AddWindow, self).__init__()
        loadUi('src/BuilderUI/Add.ui', self)
        self.satubtn= self.findChild(QPushButton, 'satu')
        self.duabtn= self.findChild(QPushButton, 'dua')
        self.tigabtn= self.findChild(QPushButton, 'tiga')
        self.fotobtn = self.findChild(QPushButton, 'inputFoto')
        self.backHome = self.findChild(QPushButton, 'backHome')
        self.pixmap = QtGui.QPixmap('src/Assets/Group 8.png')
        self.fotobtn.setIcon(QtGui.QIcon(self.pixmap))
        #set icon to fill button
        self.fotobtn.setIconSize(QtCore.QSize(385, 385))
        self.submitbtn = btn.ArrowButton()
        self.submitbtn.setGeometry(1600, 800, 150, 41)
        self.submitbtn.setParent(self)
        self.submitbtn.setText(">")
        self.submitbtn.clicked.connect(self.submitData)
        self.fotobtn.clicked.connect(self.fotoDialog)
        self.stackedWidget.setCurrentIndex(0)
        self.fileName = ""
        self.notif_container.hide()
        # Connect the button's clicked signal to a slot that switches to page 1
        self.satubtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.duabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.tigabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        
        self.inputHewan = self.findChild(QLineEdit, 'inputNama')
        self.inputJenis = self.findChild(QLineEdit, 'inputJenis')
        self.inputUmur = self.findChild(QLineEdit, 'inputUmur')
        self.inputBerat = self.findChild(QLineEdit, 'inputBerat')
        self.inputBirth = self.findChild(QLineEdit, 'inputBirth')
        self.inputGender = self.findChild(QLineEdit, 'inputGender')
        self.inputJenisMakanan = self.findChild(QLineEdit, 'inputJenisMakanan')
        self.inputNamaMakanan = self.findChild(QLineEdit, 'inputNamaMakanan')
        self.inputKesehatan = self.findChild(QLineEdit, 'inputKesehatan')
        self.inputPeriode = self.findChild(QLineEdit, 'inputPeriode')
        self.inputTanggalKesehatan = self.findChild(QLineEdit, 'inputTanggalKesehatan')
        
        self.namaHewan = self.inputHewan.text()
        self.namaJenis = self.inputJenis.text()

    
    def saveDataHewan (self):
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT count(ID) FROM Hewan")
        rows = self.cur.fetchall()
        id = rows[0][0]+1
        q1 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,gender, foto) VALUES (" + str(id) + ", '" + self.inputHewan.text() + "', '" + self.inputJenis.text() + "', " + self.inputUmur.text() + ", '" + self.inputBirth.text() + "', " + self.inputBerat.text() + ", '"+ self.inputGender.text() + "', '" + self.fileName + "')"
        self.con.execute(q1)
        self.con.commit() 
        self.con.close()

    def saveDataMakanan (self):
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT count(ID) FROM Hewan")
        rows = self.cur.fetchall()
        id = rows[0][0]+1
        q1 = "INSERT INTO Makanan (ID,jenisMakanan,namaMakanan) VALUES (" + str(id) + ", '" + self.inputJenisMakanan.text() + "', '" + self.inputNamaMakanan.text() + "')"
        self.con.execute(q1)
        self.con.commit()
        self.con.close()

    def saveDataKesehatan (self):
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT count(ID) FROM Hewan")
        rows = self.cur.fetchall()
        id = rows[0][0]+1
        q1 = "INSERT INTO Kesehatan (ID,catatanKesehatan,periode,tanggalPeriksa) VALUES (" + str(id) + ", '" + self.inputKesehatan.text() + "', '" + self.inputPeriode.text() + "', '" + self.inputTanggalKesehatan.text() + "')"
        self.con.execute(q1)
        self.con.commit()
        self.con.close()
    
    def submitData(self):
        try:
            self.saveDataHewan()
            self.saveDataMakanan()
            self.saveDataKesehatan()
            self.notif_value.setText("Data Berhasil Ditambahkan")
            self.notif_container.show()
            QTimer.singleShot(3000, lambda: self.notif_container.hide())
        except:
            self.notif_value.setText("Data Gagal Ditambahkan")
            self.notif_container.show()
            QTimer.singleShot(3000, lambda: self.notif_container.hide())

    def fotoDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.fotobtn.setIcon(QtGui.QIcon(self.fileName))
        self.fotobtn.setIconSize(QtCore.QSize(385, 385))
        
        