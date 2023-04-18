from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
import sqlite3 as mdb
import Hewan as h
import Button as btn
import Add 


class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        loadUi('src/BuilderUI/Info.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        
        
        self.indtbtn = self.findChild(QPushButton, 'info')
        self.mafabtn = self.findChild(QPushButton, 'makanan')
        self.cakebtn = self.findChild(QPushButton, 'kesehatan')
        self.editbtn = self.findChild(QPushButton,'editButton')
        self.editbtn2 = self.findChild(QPushButton,'editButton2')
        self.editbtn3 = self.findChild(QPushButton,'editButton3')
        self.addbtn = self.findChild(QPushButton,'addButton')
        self.addbtn2 = self.findChild(QPushButton,'addButton2')
        self.addbtn3= self.findChild(QPushButton,'addButton3')
        
        
        
        
        
        
        # self.foodNameLbl = self.findChild(QLabel, 'namaMakanan')
        # self.foodDescLbl = self.findChild(QLabel, 'jenisMakanan')
        # self.infoKesLbl = self.findChild(QLabel, 'infoKes')
        # self.descKesLbl = self.findChild(QLabel, 'descKes')
        
        #set ikon tombol 

        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.editbtn.setIcon(QtGui.QIcon(self.pixmap))

        self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        self.addbtn.setIcon(QtGui.QIcon(self.pixmap))

        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.editbtn2.setIcon(QtGui.QIcon(self.pixmap))

        self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        self.addbtn2.setIcon(QtGui.QIcon(self.pixmap))

        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.editbtn3.setIcon(QtGui.QIcon(self.pixmap))

        self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        self.addbtn3.setIcon(QtGui.QIcon(self.pixmap))

        self.fotoLbl = self.findChild(QLabel, 'fotoHewan')
        self.namaLbl = self.findChild(QLabel, 'nama')
        self.jenisLbl = self.findChild(QLabel, 'jenisHewan')
        self.umurLbl = self.findChild(QLabel, 'umur')
        self.birthLbl = self.findChild(QLabel, 'lahir')
        self.genderLbl = self.findChild(QLabel, 'gender')
        self.beratLbl = self.findChild(QLabel, 'berat')
        # self.editDetailInfo = self.findChild(QWidget, Add.AddWindow().__init__().stackedWidget.setCurrentIndex(0))
        self.indtbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mafabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cakebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        # self.editbtn.clicked.connect(lambda: self.editDetailInfo)


    def showData (self, ID) :
        print("bau")
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.fotoLbl = self.findChild(QLabel, 'fotoHewan')
        self.namaLbl = self.findChild(QLabel, 'nama')
        self.jenisLbl = self.findChild(QLabel, 'jenisHewan')
        self.umurLbl = self.findChild(QLabel, 'umur')
        self.birthLbl = self.findChild(QLabel, 'lahir')
        self.genderLbl = self.findChild(QLabel, 'gender')
        self.beratLbl = self.findChild(QLabel, 'berat')
        self.cur.execute("SELECT nama,jenis,umur,birthdate,berat,foto FROM Hewan WHERE ID =?", (ID,))
        self.cur.execute("SELECT foto FROM Hewan WHERE ID =?", (ID,))
        foto = self.cur.fetchone()[0]
        fotoByte = bytes(foto, encoding='utf-8')
        fotoHwn = QtGui.QPixmap()
        fotoHwn.loadFromData(fotoByte)
        self.fotoLbl.setPixmap(fotoHwn)
        self.fotoLbl.setScaledContents(True)
        self.fotoLbl.show()

        self.cur.execute("SELECT nama FROM Hewan WHERE ID =?", (ID,))
        nama = self.cur.fetchone()[0]
        self.namaLbl.setText(nama)
        self.namaLbl.show()
        
        self.cur.execute("SELECT jenis FROM Hewan WHERE ID =?", (ID,))
        jenis = self.cur.fetchone()[0]
        self.jenisLbl.setText(jenis)
        self.jenisLbl.show()

        self.cur.execute("SELECT umur FROM Hewan WHERE ID =?", (ID,))
        umur = self.cur.fetchone()[0]
        self.umurLbl.setText(str(umur))
        self.umurLbl.show()

        self.cur.execute("SELECT birthdate FROM Hewan WHERE ID =?", (ID,))
        bday = self.cur.fetchone()[0]
        self.birthLbl.setText(bday)
        self.birthLbl.show()

        self.cur.execute("SELECT berat FROM Hewan WHERE ID =?", (ID,))
        berat = self.cur.fetchone()[0]
        self.beratLbl.setText(str(berat))
        self.beratLbl.show()


        self.con.close()

        # showData(self, 2)