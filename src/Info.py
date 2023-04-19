from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
import sqlite3 as mdb
import Hewan as h
import Button as btn
from PyQt5.QtGui import QFontMetrics
import Add 
import sys
import Button as bt




class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        loadUi('src/BuilderUI/Info.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        
        self.indtbtn = self.findChild(QPushButton, 'info')
        self.mafabtn = self.findChild(QPushButton, 'makanan')
        self.cakebtn = self.findChild(QPushButton, 'kesehatan')
        # self.editbtn = self.findChild(QPushButton,'editButton')
        # self.editbtn2 = self.findChild(QPushButton,'editButton2')
        # self.editbtn3 = self.findChild(QPushButton,'editButton3')
        # self.addbtn = self.findChild(QPushButton,'addButton')
        # self.addbtn2 = self.findChild(QPushButton,'addButton2')
        # self.addbtn3= self.findChild(QPushButton,'addButton3')
        self.editbtn = bt.editButton()
        self.editbtn.setGeometry(1550,850,30,30)
        # self.editbtn.setParent(self)
        # self.editbtn.clicked.connect(self.edit)
        self.addbtn = bt.addButton()
        self.addbtn.setGeometry(1610,850,30,30)
        # self.addbtn.setParent(self)

        # self.pixmap = QtGui.QPixmap('src/Assets/edit-rev.png')
        # self.editbtn.setIcon(QtGui.QIcon(self.pixmap))
        
        # self.pixmap = QtGui.QPixmap('src/Assets/add-rev.png')
        # self.addbtn.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        # self.editbtn2.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        # self.addbtn2.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        # self.editbtn3.setIcon(QtGui.QIcon(self.pixmap))

        # self.pixmap = QtGui.QPixmap('src/Assets/add.png')
        # self.addbtn3.setIcon(QtGui.QIcon(self.pixmap))

        # self.editDetailInfo = self.findChild(QWidget, Add.AddWindow().__init__().stackedWidget.setCurrentIndex(0))
        self.indtbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mafabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cakebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        # self.editbtn.clicked.connect(lambda: self.editDetailInfo)


    def showDetail (self, ID) :
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.fotoLbl = self.findChild(QLabel, 'fotoHewan')
        self.namaLbl = self.findChild(QLabel, 'nama')
        self.jenisLbl = self.findChild(QLabel, 'jenisHewan')
        self.umurLbl = self.findChild(QLabel, 'umur')
        self.birthLbl = self.findChild(QLabel, 'lahir')
        self.genderLbl = self.findChild(QLabel, 'gender')
        self.beratLbl = self.findChild(QLabel, 'berat')

        self.cur.execute("SELECT nama,jenis,umur,birthdate,berat,gender,foto FROM Hewan WHERE ID =?", (ID,))
        nama,jenis,umur,bday,berat,gender,foto = self.cur.fetchone()
        fotoByte = bytes(foto, encoding='utf-8')
        fotoHwn = QtGui.QPixmap()
        fotoHwn.loadFromData(QByteArray.fromBase64(fotoByte), "PNG")
        self.fotoLbl.setPixmap(fotoHwn)
        self.fotoLbl.setScaledContents(True)
        self.fotoLbl.show()

        # font_metrics = QFontMetrics(self.namaLbl.font())
        # text_width = font_metrics.width(nama)
        # if text_width > self.namaLbl.width():
        #     font_size = self.namaLbl.font().pointSize()
        #     while font_metrics.width(nama) > self.namaLbl.width():
        #         font_size -= 1
        #         font = self.namaLbl.font()
        #         font.setPointSize(font_size)
        #         self.namaLbl.setFont(font) 
                   
        self.namaLbl.setText(nama)
        self.namaLbl.show()

        # font_metrics = QFontMetrics(self.jenisLbl.font())
        # text_width = font_metrics.width(jenis)
        # if text_width > self.jenisLbl.width():
        #     font_size = self.jenisLbl.font().pointSize()
        #     while font_metrics.width(jenis) > self.jenisLbl.width():
        #         font_size -= 1
        #         font = self.jenisLbl.font()
        #         font.setPointSize(font_size)
        #         self.jenisLbl.setFont(font)

        self.jenisLbl.setText(jenis)
        self.jenisLbl.show()
      
        # font_metrics = QFontMetrics(self.umurLbl.font())
        # text_width = font_metrics.width(umur)
        # if text_width > self.umurLbl.width():
        #     font_size = self.umurLbl.font().pointSize()
        #     while font_metrics.width(umur) > self.umurLbl.width():
        #         font_size -= 1
        #         font = self.umurLbl.font()
        #         font.setPointSize(font_size)
        #         self.umurLbl.setFont(font)
        self.umurLbl.setText(str(umur))
        self.umurLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.umurLbl.show()
      
        self.birthLbl.setText(bday)
        self.birthLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.birthLbl.show()

        # font_metrics = QFontMetrics(self.genderLbl.font())
        # text_width = font_metrics.width(gender)
        # if text_width > self.genderLbl.width():
        #     font_size = self.genderLbl.font().pointSize()
        #     while font_metrics.width(gender) > self.genderLbl.width():
        #         font_size -= 1
        #         font = self.genderLbl.font()
        #         font.setPointSize(font_size)
        #         self.genderLbl.setFont(font)
        self.genderLbl.setText(gender)
        self.genderLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.genderLbl.show()

        
        self.beratLbl.setText(str(berat))
        self.beratLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.beratLbl.show()

        self.con.close()
        

    def showFood (self, ID) :
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.foodLbl = self.findChild(QLabel, 'namaMakanan')
        self.foodTypeLbl = self.findChild(QLabel, 'jenisMakanan')
        self.cur.execute("SELECT namaMakanan, jenisMakanan FROM Makanan where ID = ?",(ID,))
        foodName, foodType = self.cur.fetchone()

        self.foodLbl.setText(foodName)
        # self.foodLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.foodLbl.show()
        self.foodTypeLbl.setText(foodType)
        # self.foodTypeLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.foodTypeLbl.show()

    def showHealth (self, ID) :
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.catKesLbl = self.findChild(QLabel, 'catkes')
        self.periodeLbl = self.findChild(QLabel, 'periodKes')
        self.cekDateLbl = self.findChild(QLabel, 'cekDateKes')
        self.cur.execute("SELECT CatatanKesehatan, periode, tanggalPeriksa FROM Kesehatan where ID = ?",(ID,))
        health, periode, cekDate = self.cur.fetchone()

        self.catKesLbl.setText(health)
        self.catKesLbl.show()
        self.periodeLbl.setText(periode)
        self.periodeLbl.show()
        self.cekDateLbl.setText(cekDate)
        self.cekDateLbl.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    info_window = InfoWindow()
    info_window.showDetail(3)
    info_window.exec_()

