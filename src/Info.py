from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
import sqlite3 as mdb
import Hewan as h
import Button as btn




class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        loadUi('src/BuilderUI/Info.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        

        # Menghubungkan tombol
        self.indtbtn = self.findChild(QPushButton, 'info')
        self.mafabtn = self.findChild(QPushButton, 'makanan')
        self.cakebtn = self.findChild(QPushButton, 'kesehatan')
        self.editbtn = self.findChild(QPushButton,'editButton')
        self.editbtn2 = self.findChild(QPushButton,'editButton2')
        self.editbtn3 = self.findChild(QPushButton,'editButton3')
        self.addbtn = self.findChild(QPushButton,'addButton')
        self.addbtn2 = self.findChild(QPushButton,'addButton2')
        self.addbtn3= self.findChild(QPushButton,'addButton3')

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

        self.indtbtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.mafabtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.cakebtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))


        def showDet(self, id):
        
            conn = mdb.connect('src/DataBase/Hewan.db')
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
        
        # def createCard(self):
        #     self.con = mdb.connect('src\DataBase\Hewan.db')
        #     # self.con.execute("INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) VALUES (2, 'Anjing', 'Mamalia', 3, '2018-01-02', 10, 'D:\Downloads\image 4.png')")
        #     self.cur = self.con.cursor()
        #     self.cur.execute("SELECT ID, nama, jenis, foto FROM Hewan")
        #     rows = self.cur.fetchall()
        #     i = 1
        #     self.frames = []
        #     for row in rows:
        #     # set the geometry of the frame
        #         self.frame = QFrame(self.carousel)
        #         x = (self.jumlahHewan - 1) * 480
        #         self.frame.setGeometry(QRect(x, 0, 460, 601))
        #         self.frame.setMaximumSize(460, 601)  # set the maximum size of the frame[count]
        #         self.frame.setMinimumSize(460, 601)  # set the minimum size of the frame[count]
        #         self.frame.setFrameShape(QFrame.StyledPanel)  # set a shape for the frame
        #         self.frame.setStyleSheet("background-color: #FFFFFF; opacity:1.0; border-radius: 20px; border: 2px solid rgba(0, 0, 0, 0.05);")
        #         # creating a QGraphicsDropShadowEffect object
        #         self.frames.append(self.frame)
        #         shadow = QGraphicsDropShadowEffect()

        #         # setting blur radius (optional step)
        #         shadow.setBlurRadius(15)
        #         self.frame.setGraphicsEffect(shadow)
        #         name = "frame" + str(i)
        #         self.frame.setObjectName("frame{}".format(i))
                
        #         # create Label in frame
        #         self.label = QLabel(self.frame)
        #         self.label.setGeometry(QRect(107, 60, 246, 245))
        #         self.label.setStyleSheet("border-radius: 95px; background-position: center;border : none; background-color: rgb(255, 255, 255, 0.9)")
        #         self.pixmap = QtGui.QPixmap(row[3])
        #         self.label.setPixmap(self.pixmap)
        #         # self.label.setStyleSheet("background-image:url('src/Assets/Mask group dexter (1).png')")
        #         self.label.setObjectName("label")
                
        #         self.label_3 = QLabel(self.frame)
        #         self.label_3.setGeometry(QRect(80, 410, 300, 40))
        #         self.label_3.setAlignment(Qt.AlignCenter) 
        #         self.label_3.setStyleSheet("font: 75 14pt \"Inter\"; color: rgb(0, 0, 0); border : none")
        #         self.label_3.setObjectName("label_3")
        #         self.label_3.setText(row[2])
        #         # create Label in frame
        #         self.label_2 = QLabel(self.frame)
        #         self.label_2.setGeometry(QRect(80, 350, 300, 60))
        #         self.label_2.setAlignment(Qt.AlignCenter) 
        #         self.label_2.setStyleSheet("font: 75 26pt \"Inter\"; color: rgba(60, 92, 194, 1);border : none")
        #         self.label_2.setObjectName("label_2")
        #         self.label_2.setText(row[1])

        #         self.detail = btn.DetailButton()
        #         #set detail parent to self frame
        #         self.detail.setParent(self.frame)
        #         self.namebtn = "detail" + str(i)
        #         self.detail.setGeometry(QRect(139, 490, 180, 60))
        #         self.detail.setObjectName(self.namebtn)
        #         # self.detail.setStyleSheet("backgroun")
                
        #         # add the frame to the carousel layout
        #         self.carouselLayout.setSpacing(5)
        #         self.carouselLayout.addWidget(self.frame)
        #         self.carouselLayout.setAlignment(Qt.AlignLeft)
        #         self.carouselLayout.setSpacing(20)
        #         self.carouselwidth += 480
        #         self.carousel.setGeometry(QRect(0, 200, self.carouselwidth, 631))
        #         self.carousel.setLayout(self.carouselLayout)
        #         i += 1
        #     for child in self.carousel.children():
        #         print(child.objectName())
        #     self.frame1 = self.findChild(QFrame, "frame1")
        #     self.frame2 = self.findChild(QFrame, "frame2")
        #     self.frame3 = self.findChild(QFrame, "frame3")
        #     self.frame4 = self.findChild(QFrame, "frame4")
        #     self.frame5 = self.findChild(QFrame, "frame5")
        #     self.frame6 = self.findChild(QFrame, "frame6")
        #     self.frame7 = self.findChild(QFrame, "frame7")
        #     self.frame8 = self.findChild(QFrame, "frame8")
        #     self.frame9 = self.findChild(QFrame, "frame9")
        #     self.frame10 = self.findChild(QFrame, "frame10")
        #     self.frame11 = self.findChild(QFrame, "frame11")
        #     self.button1 = self.findChild(btn.DetailButton, "detail1")
        #     self.button2 = self.findChild(btn.DetailButton, "detail2")
        #     self.button3 = self.findChild(btn.DetailButton, "detail3")
        #     self.button4 = self.findChild(btn.DetailButton, "detail4")
        #     self.button5 = self.findChild(btn.DetailButton, "detail5")
        #     self.button6 = self.findChild(btn.DetailButton, "detail6")
        #     self.button7 = self.findChild(btn.DetailButton, "detail7")
        #     self.button8 = self.findChild(btn.DetailButton, "detail8")
        #     self.button9 = self.findChild(btn.DetailButton, "detail9")
        #     self.button10 = self.findChild(btn.DetailButton, "detail10")
        #     self.button11 = self.findChild(btn.DetailButton, "detail11")
        #     if self.frames.count == 1:
        #         self.frame1.hide()
        #     elif self.frames.count == 2:
        #         self.frame2.hide()
        #     elif self.frames.count == 3:
        #         self.frame3.hide()
        #     elif self.frames.count == 4:
        #         self.frame4.hide()
        #     # self.animasi1 = self.animate(self.frame1, 0)
        #     # self.animasi2 = self.animate(self.frame2, 480)
        #     # self.animasi3 = self.animate(self.frame3, 960)
        #     # self.animasi4 = self.animate(self.frame4, 1440)
        
        #     self.group_animation = QParallelAnimationGroup()
        #     j = 0
        #     for frame in self.frames:
                
        #         self.animation = QPropertyAnimation(frame, b"pos")
        #         self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        #         self.animation.setStartValue(QPoint(1920, 0))
        #         self.animation.setEndValue(QPoint(j,0))
        #         self.animation.setDuration(1300)
        #         self.group_animation.addAnimation(self.animation)
        #         j += 480
        #     self.group_animation.start()
        #     self.con.close()
