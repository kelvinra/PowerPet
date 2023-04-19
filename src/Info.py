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
        
        self.idData = 0
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

        # self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        # self.editbtn.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        # self.addbtn.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        # self.editbtn2.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        # self.addbtn2.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        # self.editbtn3.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        # self.addbtn3.setIcon(QtGui.QIcon(self.pixmap))

        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit.setIcon(QtGui.QIcon(self.pixmap))
        self.edit.clicked.connect(self.editTextUmur)
        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit_2.setIcon(QtGui.QIcon(self.pixmap))
        self.edit_2.clicked.connect(self.editTextGender)
        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit_3.setIcon(QtGui.QIcon(self.pixmap))
        self.edit_3.clicked.connect(self.editTextLahir)
        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit_4.setIcon(QtGui.QIcon(self.pixmap))
        self.edit_4.clicked.connect(self.editTextBerat)

        self.fotoLbl = self.findChild(QLabel, 'fotoHewan')
        self.namaLbl = self.findChild(QLabel, 'nama')
        self.jenisLbl = self.findChild(QLabel, 'jenisHewan')
        self.birthLbl = self.findChild(QLabel, 'lahir')
        self.genderLbl = self.findChild(QLabel, 'gender')
        self.beratLbl = self.findChild(QLabel, 'berat')
        self.umurLbl = self.findChild(QLabel, 'umur')
        # self.editDetailInfo = self.findChild(QWidget, Add.AddWindow().__init__().stackedWidget.setCurrentIndex(0))
        self.indtbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mafabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cakebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        # self.editbtn.clicked.connect(lambda: self.editDetailInfo)
        self.editumur.setEnabled(False)
        self.editgender.setEnabled(False)
        self.editberat.setEnabled(False)
        self.editlahir.setEnabled(False)


    def showData (self, ID) :
        print("bau")
        self.idData = ID
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.fotoLbl = self.findChild(QLabel, 'fotoHewan')
        self.namaLbl = self.findChild(QLabel, 'nama')
        self.jenisLbl = self.findChild(QLabel, 'jenisHewan')
        # self.umurLbl = self.findChild(QLabel, 'umur')
        self.birthLbl = self.findChild(QLabel, 'lahir')
        self.genderLbl = self.findChild(QLabel, 'gender')
        self.beratLbl = self.findChild(QLabel, 'berat')
        self.cur.execute("SELECT nama,jenis,umur,birthdate,berat,foto FROM Hewan WHERE ID =?", (ID,))
        self.cur.execute("SELECT foto FROM Hewan WHERE ID =?", (ID,))
        foto = self.cur.fetchone()[0]
        self.fotoLbl.setPixmap(QtGui.QPixmap(foto))

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
        self.editumur.setText(str(umur))
        # self.umurLbl.setText(str(umur))
        # self.umurLbl.show()

        self.cur.execute("SELECT birthdate FROM Hewan WHERE ID =?", (ID,))
        bday = self.cur.fetchone()[0]
        self.editlahir.setText(bday)
        # self.birthLbl.setText(bday)
        # self.birthLbl.show()

        self.cur.execute("SELECT berat FROM Hewan WHERE ID =?", (ID,))
        berat = self.cur.fetchone()[0]
        self.editberat.setText(str(berat))
        # self.beratLbl.setText(str(berat))
        # self.beratLbl.show()

        self.cur.execute("SELECT gender FROM Hewan WHERE ID =?", (ID,))
        gender = self.cur.fetchone()[0]
        self.editgender.setText(str(gender))
        # self.genderLbl.setText(str(gender))
        # self.genderLbl.show()

        self.cur.execute("SELECT jenisMakanan FROM Makanan WHERE ID =?", (ID,))
        makanan = self.cur.fetchone()[0]



        self.con.close()


    def editTextUmur(self):
        if self.editumur.isEnabled():
            self.editumur.setEnabled(False)
        else:
            self.editumur.setEnabled(True)
            self.editumur.show()
            self.editumur.setFocus()
            self.editumur.editingFinished.connect(self.editUmur)
    
    def editTextGender(self):
        if self.editgender.isEnabled():
            self.editgender.setEnabled(False)
        else:
            self.editgender.setEnabled(True)
            self.editgender.show()
            self.editgender.setFocus()
            self.editgender.editingFinished.connect(self.editGender)

    def editTextLahir(self):
        if self.editlahir.isEnabled():
            self.editlahir.setEnabled(False)
        else:
            self.editlahir.setEnabled(True)
            self.editlahir.show()
            self.editlahir.setFocus()
            self.editlahir.editingFinished.connect(self.editLahir)

    def editTextBerat(self):
        if self.editberat.isEnabled():
            self.editberat.setEnabled(False)
        else:
            self.editberat.setEnabled(True)
            self.editberat.show()
            self.editberat.setFocus()
            self.editberat.editingFinished.connect(self.editBerat)

    def editBerat(self):
        # self.editberat.setEnabled(False)
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Hewan SET berat = ? WHERE ID = ?", (self.editberat.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData)

    def editLahir(self):
        # self.editlahir.setEnabled(False)
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Hewan SET birthdate = ? WHERE ID = ?", (self.editlahir.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData)

    def editGender(self):
        # self.editgender.setEnabled(False)
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Hewan SET gender = ? WHERE ID = ?", (self.editgender.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData) 
    
    def editUmur(self):
        # self.editumur.setEnabled(False)
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Hewan SET umur = ? WHERE ID = ?", (self.editumur.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData)
    
    