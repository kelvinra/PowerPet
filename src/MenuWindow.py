import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import Hewan as h
import sqlite3 as mdb

class MenuWindow(QDialog):
    def __init__(self):
        
        super(MenuWindow, self).__init__()
        loadUi('src\BuilderUI\Menu.ui', self)
        self.Arrow.clicked.connect(self.slideleft)
        self.Arrow_2.clicked.connect(self.slideright)
        # QtCore.QTimer.singleShot(100, self.slideright)
        self.poscarosel = 0
        self.jumlahHewan = 0
        self.Add.clicked.connect(self.createCard)
        self.carouselwidth = 1920

        # set the QStackedLayout as the layout for the carousel widget
        self.carouselLayout = QHBoxLayout(self.carousel)
        self.carouselLayout.setSpacing(15)
        self.carouselLayout.setContentsMargins(0, 0, 0, 0)
        self.carouselLayout.setObjectName("carouselLayout")
        self.carousel.setLayout(self.carouselLayout)

    def slideleft(self):
        self.animation = QPropertyAnimation(self.carousel, b"pos")
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(self.poscarosel, 250))
        self.poscarosel += 480
        self.animation.setEndValue(QPoint(self.poscarosel,250))
        self.animation.setDuration(500)
        self.animation.start()

    def slideright(self):
        self.animation = QPropertyAnimation(self.carousel, b"pos")
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(self.poscarosel, 250))
        self.poscarosel -= 480
        self.animation.setEndValue(QPoint(self.poscarosel,250))
        self.animation.setDuration(500)
        self.animation.start()

    def createCard(self):
        self.con = mdb.connect('src\DataBase\Hewan.db')
        # self.con.execute("INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) VALUES (2, 'Anjing', 'Mamalia', 3, '2018-01-02', 10, 'D:\Downloads\image 4.png')")
        self.cur = self.con.cursor()
        self.cur.execute("SELECT ID, nama, jenis, foto FROM Hewan")
        print (self.cur.rowcount)
        rows = self.cur.fetchall()
        print(len(rows))
        for row in rows:
        # set the geometry of the frame
            self.frame = QFrame(self.carousel)
            x = (self.jumlahHewan - 1) * 480
            self.frame.setGeometry(QRect(x, 0, 470, 631))
            self.frame.setMaximumSize(460, 631)  # set the maximum size of the frame[count]
            self.frame.setMinimumSize(460, 631)  # set the minimum size of the frame[count]
            self.frame.setStyleSheet("background-color: rgb(220, 220, 220); border-radius: 15px;")
            self.frame.setObjectName("frame")
            
            # create Label in frame
            self.label = QLabel(self.frame)
            self.label.setGeometry(QRect(80, 30, 300, 300))
            self.label.setStyleSheet(" border-radius: 95px;")
            self.pixmap = QtGui.QPixmap(row[3])
            self.label.setPixmap(self.pixmap)
            # self.label.setStyleSheet("background-image:url('src/Assets/Mask group dexter (1).png')")
            self.label.setObjectName("label")
            
            self.label_3 = QLabel(self.frame)
            self.label_3.setGeometry(QRect(190, 430, 100, 40))
            self.label_3.setStyleSheet("font: 75 14pt \"Inter\"; color: rgb(0, 0, 0);")
            self.label_3.setObjectName("label_3")
            self.label_3.setText(row[2])
            # create Label in frame
            self.label_2 = QLabel(self.frame)
            self.label_2.setGeometry(QRect(150, 350, 180, 60))
            self.label_2.setStyleSheet("font: 75 30pt \"Inter\"; color: rgb(0, 0, 0);")
            self.label_2.setObjectName("label_2")
            self.label_2.setText(row[1])
            
            # add the frame to the carousel layout
            self.carouselLayout.setSpacing(5)
            self.carouselLayout.addWidget(self.frame)
            self.carouselLayout.setAlignment(Qt.AlignLeft)
            self.carouselLayout.setSpacing(20)
            self.carouselwidth += 480
            self.carousel.setGeometry(QRect(0, 250, self.carouselwidth, 631))
            self.carousel.setLayout(self.carouselLayout)
        
        self.con.close()



    def tambahHewan(self):
        self.hewan = h.Hewan(1, "Kucing", "Kucing", "Daging", 1, "1/1/2019", "Jantan", 10)
        print(self.jumlahHewan)
        self.jumlahHewan += 1
        self.createCard()
        print(self.carousel.layout().count())

    def DBConnect(self):
        self.con = mdb.connect('src\DataBase\Hewan.db')
        self.cur = self.con.execute("SELECT * FROM Hewan")
        self.con.close()
