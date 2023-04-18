import sys
from PyQt5 import sip
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import Hewan as h
import Button as btn
import sqlite3 as mdb

class MenuWindow(QDialog):
    def __init__(self):
        
        super(MenuWindow, self).__init__()
        loadUi('src\BuilderUI\Menu.ui', self)
        self.Arrow1 = btn.ArrowButton()
        self.Arrow1.setGeometry(20,860,80,80)
        self.Arrow1.setParent(self)
        self.Arrow2 = btn.ArrowButton()
        self.Arrow2.setGeometry(1793,860,50,50)
        self.Arrow2.setText(">")
        self.Arrow2.setParent(self)
        self.Arrow1.clicked.connect(self.slideleft)
        self.Arrow2.clicked.connect(self.slideright)
        self.Add = btn.AddHButton()
        self.Add.setGeometry(1600,80,150,41)
        self.Add.setParent(self)
        self.filter.clicked.connect(self.sidebaranimate)
        self.search.clicked.connect(self.filterHewan)
        # QtCore.QTimer.singleShot(100, self.slideright)
        self.poscarosel = 0
        self.jumlahHewan = 0
        self.carouselwidth = 1920
        self.carousel = QFrame(self)
        self.sidebarcounter = 0
        self.frames = []
        self.buttons = []
        

        # set the QStackedLayout as the layout for the carousel widget
    def populateFrame(self):
        self.deleteLayout(self.frame.layout())
        layout = QtGui.QVBoxLayout(self.frame)
        ...

    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(layout)
        
    def showEvent(self, event):
        self.deleteLayout(self.carousel.layout())
        self.carousel.setGeometry(QRect(0, self.poscarosel, 1920, 631))
        self.carouselLayout = QHBoxLayout(self.carousel)
        self.carouselLayout.setSpacing(15)
        self.carouselLayout.setContentsMargins(0, 0, 0, 0)
        self.carouselLayout.setObjectName("carouselLayout")
        self.carousel.setLayout(self.carouselLayout)
        self.frames.clear()
        self.buttons.clear()
        self.createCard()

    def slideleft(self):
        self.animation = QPropertyAnimation(self.carousel, b"pos")
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(self.poscarosel, 200))
        self.poscarosel += 480
        self.animation.setEndValue(QPoint(self.poscarosel,200))
        self.animation.setDuration(1000)
        self.animation.start()

    def slideright(self):
        self.animation = QPropertyAnimation(self.carousel, b"pos")
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(self.poscarosel, 200))
        self.poscarosel -= 480
        self.animation.setEndValue(QPoint(self.poscarosel,200))
        self.animation.setDuration(1000)
        self.animation.start()

    # def animate(self, widget, pos):
    #     widget.show()
    #     self.animation = QPropertyAnimation(widget, b"pos")
    #     self.animation.setEasingCurve(QEasingCurve.InOutCubic)
    #     self.animation.setStartValue(QPoint(1920, 0))
    #     self.animation.setEndValue(QPoint(pos,0))
    #     self.animation.setDuration(1000)

    def sidebaranimate(self):
        if self.sidebarcounter == 0:
            self.animation = QPropertyAnimation(self.sidebar, b"minimumWidth")
            self.animation.setEasingCurve(QEasingCurve.InOutCubic)
            self.animation.setStartValue(91)
            self.animation.setEndValue(581)
            self.animation.setDuration(500)
            self.animation.start()
            self.animation1 = QPropertyAnimation(self.sidebar, b"maximumWidth")
            self.animation1.setEasingCurve(QEasingCurve.InOutCubic)
            self.animation1.setStartValue(91)
            self.animation1.setEndValue(581)
            self.animation1.setDuration(500)
            self.animation1.start()
            self.sidebarcounter = 1
        else:
            self.animation = QPropertyAnimation(self.sidebar, b"minimumWidth")
            self.animation.setEasingCurve(QEasingCurve.InOutCubic)
            self.animation.setStartValue(self.sidebar.width())
            self.animation.setEndValue(91)
            self.animation.setDuration(500)
            self.animation.start()
            self.animation1 = QPropertyAnimation(self.sidebar, b"maximumWidth")
            self.animation1.setEasingCurve(QEasingCurve.InOutCubic)
            self.animation1.setStartValue(self.sidebar.width())
            self.animation1.setEndValue(91)
            self.animation1.setDuration(500)
            self.animation1.start()
            self.sidebarcounter = 0
        

    def createCard(self):
        self.con = mdb.connect('src\DataBase\Hewan.db')
        # self.con.execute("INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) VALUES (2, 'Anjing', 'Mamalia', 3, '2018-01-02', 10, 'D:\Downloads\image 4.png')")
        self.cur = self.con.cursor()
        self.cur.execute("SELECT ID, nama, jenis, foto FROM Hewan")
        rows = self.cur.fetchall()
        i = 1
        self.frames = []
        self.buttons = []
        for row in rows:
        # set the geometry of the frame
            self.frame = QFrame(self.carousel)
            x = (self.jumlahHewan - 1) * 480
            self.frame.setGeometry(QRect(x, 0, 460, 601))
            self.frame.setMaximumSize(460, 601)  # set the maximum size of the frame[count]
            self.frame.setMinimumSize(460, 601)  # set the minimum size of the frame[count]
            self.frame.setFrameShape(QFrame.StyledPanel)  # set a shape for the frame
            self.frame.setStyleSheet("background-color: #FFFFFF; opacity:1.0; border-radius: 20px; border: 2px solid rgba(0, 0, 0, 0.05);")
            # creating a QGraphicsDropShadowEffect object
            self.frames.append(self.frame)
            shadow = QGraphicsDropShadowEffect()

            # setting blur radius (optional step)
            shadow.setBlurRadius(15)
            self.frame.setGraphicsEffect(shadow)
            name = "frame" + str(i)
            self.frame.setObjectName("frame{}".format(i))
            
            # create Label in frame
            self.label = QLabel(self.frame)
            self.label.setGeometry(QRect(107, 60, 246, 245))
            self.label.setStyleSheet("border-radius: 95px; background-position: center;border : none; background-color: rgb(255, 255, 255, 0.9)")
            self.pixmap = QtGui.QPixmap(row[3])
            self.label.setPixmap(self.pixmap)
            # self.label.setStyleSheet("background-image:url('src/Assets/Mask group dexter (1).png')")
            self.label.setObjectName("label")
            
            self.label_3 = QLabel(self.frame)
            self.label_3.setGeometry(QRect(80, 410, 300, 40))
            self.label_3.setAlignment(Qt.AlignCenter) 
            self.label_3.setStyleSheet("font: 75 14pt \"Inter\"; color: rgb(0, 0, 0); border : none")
            self.label_3.setObjectName("label_3")
            self.label_3.setText(row[2])
            # create Label in frame
            self.label_2 = QLabel(self.frame)
            self.label_2.setGeometry(QRect(80, 350, 300, 60))
            self.label_2.setAlignment(Qt.AlignCenter) 
            self.label_2.setStyleSheet("font: 75 26pt \"Inter\"; color: rgba(60, 92, 194, 1);border : none")
            self.label_2.setObjectName("label_2")
            self.label_2.setText(row[1])

            self.detail = btn.DetailButton()
            #set detail parent to self frame
            self.detail.setParent(self.frame)
            self.namebtn = "detail" + str(i)
            self.detail.setGeometry(QRect(139, 490, 180, 60))
            self.detail.setObjectName(self.namebtn)
            self.buttons.append(self.detail)
            # self.detail.setStyleSheet("backgroun")
            
            # add the frame to the carousel layout
            self.carouselLayout.setSpacing(5)
            self.carouselLayout.addWidget(self.frame)
            self.carouselLayout.setAlignment(Qt.AlignLeft)
            self.carouselLayout.setSpacing(20)
            self.carouselwidth += 480
            self.carousel.setGeometry(QRect(0, 200, self.carouselwidth, 631))
            self.carousel.setLayout(self.carouselLayout)
            i += 1
        
        self.frame1 = self.findChild(QFrame, "frame1")
        self.frame2 = self.findChild(QFrame, "frame2")
        self.frame3 = self.findChild(QFrame, "frame3")
        self.frame4 = self.findChild(QFrame, "frame4")
        self.frame5 = self.findChild(QFrame, "frame5")
        self.frame6 = self.findChild(QFrame, "frame6")
        self.frame7 = self.findChild(QFrame, "frame7")
        self.frame8 = self.findChild(QFrame, "frame8")
        self.frame9 = self.findChild(QFrame, "frame9")
        self.frame10 = self.findChild(QFrame, "frame10")
        self.frame11 = self.findChild(QFrame, "frame11")
        self.button1 = self.findChild(btn.DetailButton, "detail1")
        self.button2 = self.findChild(btn.DetailButton, "detail2")
        self.button3 = self.findChild(btn.DetailButton, "detail3")
        self.button4 = self.findChild(btn.DetailButton, "detail4")
        self.button5 = self.findChild(btn.DetailButton, "detail5")
        self.button6 = self.findChild(btn.DetailButton, "detail6")
        self.button7 = self.findChild(btn.DetailButton, "detail7")
        self.button8 = self.findChild(btn.DetailButton, "detail8")
        self.button9 = self.findChild(btn.DetailButton, "detail9")
        self.button10 = self.findChild(btn.DetailButton, "detail10")
        self.button11 = self.findChild(btn.DetailButton, "detail11")
        if self.frames.count == 1:
            self.frame1.hide()
        elif self.frames.count == 2:
            self.frame2.hide()
        elif self.frames.count == 3:
            self.frame3.hide()
        elif self.frames.count == 4:
            self.frame4.hide()
        # self.animasi1 = self.animate(self.frame1, 0)
        # self.animasi2 = self.animate(self.frame2, 480)
        # self.animasi3 = self.animate(self.frame3, 960)
        # self.animasi4 = self.animate(self.frame4, 1440)
    
        self.group_animation = QParallelAnimationGroup()
        j = 0
        for frame in self.frames:
            
            self.animation = QPropertyAnimation(frame, b"pos")
            self.animation.setEasingCurve(QEasingCurve.InOutCubic)
            self.animation.setStartValue(QPoint(1920, 0))
            self.animation.setEndValue(QPoint(j,0))
            self.animation.setDuration(1300)
            self.group_animation.addAnimation(self.animation)
            j += 480
        self.group_animation.start()
        self.con.close()

    

    def filterHewan(self):
        self.con = mdb.connect('src\DataBase\Hewan.db')
        # self.con.execute("INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) VALUES (2, 'Anjing', 'Mamalia', 3, '2018-01-02', 10, 'D:\Downloads\image 4.png')")
        self.cur = self.con.cursor()
        rows = self.cur.fetchall()
        if len(self.inputj.text()) != 0:
            print("masuk")
            if len(self.inputm.text()) != 0:
                self.cur.execute("SELECT ID FROM Hewan natural join Makanan WHERE jenis ='" + self.inputj.text()+ "' AND jenisMakanan ='" + self.inputm.text()+ "'")
                rows = self.cur.fetchall()
        
                for row in rows:
                    for i in range (0, len(self.frames)):
                        if row[0] == i+1:
                            self.frames[i].show()
                        else:
                            self.frames[i].hide()
            else:
                self.cur.execute("SELECT ID FROM Hewan WHERE jenis ='" + self.inputj.text()+ "'")
                rows = self.cur.fetchall()
        
                for row in rows:
                    for i in range (0, len(self.frames)):
                        if row[0] == i+1:
                            self.frames[i].show()
                        else:
                            self.frames[i].hide()
        elif len(self.inputm.text()) != 0:
            self.cur.execute("SELECT ID FROM Makanan WHERE jenisMakanan ='" + self.inputm.text()+ "'")
            rows = self.cur.fetchall()
            for row in rows:
                for i in range (0, len(self.frames)):
                    if row[0] == i+1:
                        self.frames[i].show()
                    else:
                        self.frames[i].hide()
        else :
            for i in range (0, len(self.frames)):
                self.frames[i].show()


    def DBConnect(self):
        self.con = mdb.connect('src\DataBase\Hewan.db')
        self.cur = self.con.execute("SELECT * FROM Hewan")
        self.con.close()
