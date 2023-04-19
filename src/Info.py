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
        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit_5.setIcon(QtGui.QIcon(self.pixmap))
        self.edit_5.clicked.connect(self.editTextJenisMakanan)
        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit_6.setIcon(QtGui.QIcon(self.pixmap))
        self.edit_6.clicked.connect(self.editTextNamaMakanan)
        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit_7.setIcon(QtGui.QIcon(self.pixmap))
        self.edit_7.clicked.connect(self.editTextNama)
        self.pixmap = QtGui.QPixmap('src/Assets/edit.png')
        self.edit_8.setIcon(QtGui.QIcon(self.pixmap))
        self.edit_8.clicked.connect(self.editTextJenis)

        self.fotoLbl = self.findChild(QLabel, 'fotoHewan')
        self.namaLbl = self.findChild(QLabel, 'nama')
        self.jenisLbl = self.findChild(QLabel, 'jenisHewan')
        self.birthLbl = self.findChild(QLabel, 'lahir')
        self.genderLbl = self.findChild(QLabel, 'gender')
        self.beratLbl = self.findChild(QLabel, 'berat')
        self.umurLbl = self.findChild(QLabel, 'umur')

        self.catKesLayout = self.findChild(QVBoxLayout, 'cardLayout_5')
        self.catKesLayout.setSpacing(20)

        self.catKesContainer = QtWidgets.QWidget()
        self.catKesContainer.setStyleSheet("background-color: transparent;")
        self.catKesContainer.setLayout(self.catKesLayout)

        self.catKesScrollArea = self.findChild(QtWidgets.QScrollArea, "scrollArea")
        self.scrollArea.setWidget(self.catKesContainer)

        # make the cardLayout items always on top
        self.catKesLayout.setAlignment(QtCore.Qt.AlignTop)
        self.catKesScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)

        # self.editDetailInfo = self.findChild(QWidget, Add.AddWindow().__init__().stackedWidget.setCurrentIndex(0))
        self.indtbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mafabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cakebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        # self.editbtn.clicked.connect(lambda: self.editDetailInfo)
        self.editnama.setEnabled(False)

        self.editjenis.setEnabled(False)
        self.editumur.setEnabled(False)
        self.editgender.setEnabled(False)
        self.editberat.setEnabled(False)
        self.editlahir.setEnabled(False)
        self.editjenismakanan.setEnabled(False)
        self.editnamamakanan.setEnabled(False)



    def showData (self, ID) :
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
        self.editnama.setText(nama)
        # self.namaLbl.show()
        
        self.cur.execute("SELECT jenis FROM Hewan WHERE ID =?", (ID,))
        jenis = self.cur.fetchone()[0]
        self.editjenis.setText(jenis)
        # self.jenisLbl.show()

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
        self.editjenismakanan.setText(makanan)
        
        self.cur.execute("SELECT namaMakanan FROM Makanan WHERE ID =?", (ID,))
        namamakanan = self.cur.fetchone()[0]
        self.editnamamakanan.setText(namamakanan)

        self.addcatkesButton = self.findChild(QPushButton, 'addCatkesButton')
        self.addcatkesButton.clicked.connect(self.add_catkes_empty_card)

        self.update_catkes_cards()

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
    
    def editTextJenisMakanan(self):
        if self.editjenismakanan.isEnabled():
            self.editjenismakanan.setEnabled(False)
        else:
            self.editjenismakanan.setEnabled(True)
            self.editjenismakanan.show()
            self.editjenismakanan.setFocus()
            self.editjenismakanan.editingFinished.connect(self.editJenisMakanan)

    def editTextNamaMakanan(self):
        if self.editnamamakanan.isEnabled():
            self.editnamamakanan.setEnabled(False)
        else:
            self.editnamamakanan.setEnabled(True)
            self.editnamamakanan.show()
            self.editnamamakanan.setFocus()
            self.editnamamakanan.editingFinished.connect(self.editNamaMakanan)
    
    def editTextNama(self):
        if self.editnama.isEnabled():
            self.editnama.setEnabled(False)
        else:
            self.editnama.setEnabled(True)
            self.editnama.show()
            self.editnama.setFocus()
            self.editnama.editingFinished.connect(self.editNama)
    
    def editTextJenis(self):
        if self.editjenis.isEnabled():
            self.editjenis.setEnabled(False)
        else:
            self.editjenis.setEnabled(True)
            self.editjenis.show()
            self.editjenis.setFocus()
            self.editjenis.editingFinished.connect(self.editJenis)
    
    def editNama(self):
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Hewan SET nama = ? WHERE ID = ?", (self.editnama.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData)
    
    def editJenis(self):
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Hewan SET jenis = ? WHERE ID = ?", (self.editjenis.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData)

    def editJenisMakanan(self):
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Makanan SET jenisMakanan = ? WHERE ID = ?", (self.editjenismakanan.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData)
    
    def editNamaMakanan(self):
        self.con = mdb.connect('src/DataBase/Hewan.db')
        self.cur = self.con.cursor()
        self.cur.execute("UPDATE Makanan SET namaMakanan = ? WHERE ID = ?", (self.editnamamakanan.text(), self.idData))
        self.con.commit()
        self.con.close()
        self.showData(self.idData)

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
    
    def load_catkes_data(self):
        con = mdb.connect("src/DataBase/Hewan.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Kesehatan WHERE ID_Hewan = ?", (self.idData,))
        data = cur.fetchall()
        con.close()
        return data
    
    def add_catkes_card(self, catatan, periode, tanggal):
        card = QtWidgets.QWidget()
        # set min max card size
        card.setMinimumSize(493, 86)
        card.setMaximumSize(493, 86)
        card.setStyleSheet("background-color: #FFFFFF; border-radius: 20px;")
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # add shadow to the card
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(4)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        card.setGraphicsEffect(shadow)

        layout = QtWidgets.QHBoxLayout()

        layout1 = QtWidgets.QVBoxLayout()
        layout1.setAlignment(QtCore.Qt.AlignTop)
        layout1.setSpacing(0)

        layout2 = QtWidgets.QVBoxLayout()
        layout2.setAlignment(QtCore.Qt.AlignTop)
        layout2.setSpacing(0)

        layout3 = QtWidgets.QVBoxLayout()
        layout3.setAlignment(QtCore.Qt.AlignTop)
        layout3.setSpacing(0)

        layout4 = QtWidgets.QVBoxLayout()
        layout4.setAlignment(QtCore.Qt.AlignTop)
        layout4.setSpacing(0)

        catatan_label = QtWidgets.QLineEdit(catatan)
        catatan_label.setStyleSheet("color: black; font-size: 24px; font-family: Inter;")
        catatan_label.setReadOnly(True)
        catatan_label.setObjectName("catatan")
        
        periode_label = QtWidgets.QLineEdit(periode)
        periode_label.setStyleSheet("color: black; font-size: 28px; font-weight: bold; font-family: Inter;")
        periode_label.setReadOnly(True)
        periode_label.setObjectName("periode")

        tanggal_label = QtWidgets.QLineEdit(tanggal)
        tanggal_label.setStyleSheet("color: black; font-size: 20px; font-family: Inter; font-weight: 300;")
        tanggal_label.setReadOnly(True)
        tanggal_label.setObjectName("tanggal")

        per_label = QtWidgets.QLabel("per")
        per_label.setStyleSheet("color: black; font-size: 10px; font-family: Inter;")
        bulan_label = QtWidgets.QLabel("bulan")
        bulan_label.setStyleSheet("color: black; font-size: 12px; font-family: Inter;")

        edit_button = QtWidgets.QPushButton("Edit")
        edit_button.clicked.connect(lambda: self.edit_card(card))
        edit_button.setObjectName("edit")
        edit_button.setStyleSheet("QPushButton {color: #FFFFFF; font-family: Inter; font-size: 12px; background-color: gray; border-radius: 5px; padding: 5px; margin: 5px; border: 1px solid black;} QPushButton:hover {background-color: #FFFFFF; color: black;}")
        delete_button = QtWidgets.QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_card(card))
        delete_button.setStyleSheet("QPushButton {color: #FFFFFF; font-size: 12px; font-family: Inter; background-color: gray; border-radius: 5px; padding: 5px; margin: 5px; border: 1px solid black;} QPushButton:hover {background-color: #FFFFFF; color: black;}")

        layout1.addWidget(tanggal_label)

        layout2.addWidget(per_label)
        layout2.addWidget(periode_label)
        layout2.addWidget(bulan_label)

        layout3.addWidget(catatan_label)

        layout4.addWidget(edit_button)
        layout4.addWidget(delete_button)

        layout1.setAlignment(QtCore.Qt.AlignCenter)
        layout2.setAlignment(QtCore.Qt.AlignCenter)
        layout3.setAlignment(QtCore.Qt.AlignCenter)
        layout4.setAlignment(QtCore.Qt.AlignCenter)

        layout.addLayout(layout1, 6)
        layout.addLayout(layout2, 3)
        layout.addLayout(layout3, 6)
        layout.addLayout(layout4, 2)

        #make the tanggal horizontally and vertically centered


        card.setLayout(layout)

        self.catKesLayout.addWidget(card)
    
    def edit_card(self, card):
        catatan = card.findChild(QtWidgets.QLineEdit, "catatan")
        periode = card.findChild(QtWidgets.QLineEdit, "periode")
        tanggal = card.findChild(QtWidgets.QLineEdit, "tanggal")
        cTemp = catatan.text()
        pTemp = periode.text()
        tTemp = tanggal.text()
        catatan.setReadOnly(False)
        periode.setReadOnly(False)
        tanggal.setReadOnly(False)
        edit_button = card.findChild(QtWidgets.QPushButton, "edit")
        edit_button.setText("Save")
        edit_button.clicked.connect(lambda: self.save_card(cTemp, pTemp, tTemp, card))

    def save_card(self, c, p, t, card):
        catatan = card.findChild(QtWidgets.QLineEdit, "catatan")
        periode = card.findChild(QtWidgets.QLineEdit, "periode")
        tanggal = card.findChild(QtWidgets.QLineEdit, "tanggal")
        catatan.setReadOnly(True)
        periode.setReadOnly(True)
        tanggal.setReadOnly(True)
        edit_button = card.findChild(QtWidgets.QPushButton, "edit")
        edit_button.setText("Edit")
        edit_button.clicked.connect(lambda: self.edit_card(card))
        con = mdb.connect("src/DataBase/Hewan.db")
        cur = con.cursor()
        if c == "" and p == "" and t == "":
            cur.execute("INSERT INTO Kesehatan (ID_Hewan, catatan, periode, tanggal) VALUES (?, ?, ?, ?)", (self.idData, catatan.text(), periode.text(), tanggal.text()))
        else:
            cur.execute("UPDATE Kesehatan SET catatan = ?, periode = ?, tanggal = ? WHERE ID_Hewan = ? AND catatan = ? AND periode = ? AND tanggal = ?", (catatan.text(), periode.text(), tanggal.text(), self.idData, c, p, t))
        con.commit()
        con.close()   

    def delete_card(self, card):
        self.catKesLayout.removeWidget(card)
        card.deleteLater()
        catatan = card.findChild(QtWidgets.QLineEdit, "catatan")
        periode = card.findChild(QtWidgets.QLineEdit, "periode")
        tanggal = card.findChild(QtWidgets.QLineEdit, "tanggal")
        con = mdb.connect("src/DataBase/Hewan.db")
        cur = con.cursor()
        cur.execute("DELETE FROM Kesehatan WHERE ID_Hewan = ? AND Catatan = ? AND Periode = ? AND Tanggal = ?", (self.idData, catatan.text(), periode.text(), tanggal.text()))
        con.commit()
        con.close()

    def delete_catkes_cards(self):
        for i in reversed(range(self.catKesLayout.count())): 
            self.catKesLayout.itemAt(i).widget().setParent(None)
    
    def update_catkes_cards(self):
        self.delete_catkes_cards()
        data = self.load_catkes_data()
        for catkes in data:
            self.add_catkes_card(catkes[2], catkes[3], catkes[4])

    def add_catkes_empty_card(self):
        self.add_catkes_card("", "", "")