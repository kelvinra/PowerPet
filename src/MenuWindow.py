import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import Hewan as h

class MenuWindow(QDialog):
    def __init__(self):
        
        super(MenuWindow, self).__init__()
        loadUi('src\BuilderUI\Menu.ui', self)
        self.Arrow.clicked.connect(self.slideleft)
        self.Arrow_2.clicked.connect(self.slideright)
        # QtCore.QTimer.singleShot(100, self.slideright)
        self.poscarosel = 0
        self.jumlahHewan = 0
        self.Add.clicked.connect(self.tambahHewan)
        self.carouselwidth = 1920

        # set the QStackedLayout as the layout for the carousel widget
        self.carouselLayout = QHBoxLayout(self.carousel)
        self.carouselLayout.setSpacing(5)
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

    def createCard(self, index):
        
        
        # calculate the size of the carousel widget
        carousel_size = self.carousel.size()
        frame_width = 460
        frame_height = 631
        
        # center the frame horizontally and vertically in the carousel widget
        
        
        # set the geometry of the frame
        self.frame = QFrame(self.carousel)
        x = (self.jumlahHewan - 1) * 480
        self.frame.setGeometry(QRect(x, 0, 460, 631))
        self.frame.setMaximumSize(460, 631)  # set the maximum size of the frame[count]
        self.frame.setMinimumSize(460, 631)  # set the minimum size of the frame[count]
        self.frame.setStyleSheet("background-color: rgb(220, 220, 220); border-radius: 15px;")
        self.frame.setObjectName("frame")
        
        # create Label in frame
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(90, 30, 300, 300))
        self.label.setStyleSheet("background-image:url('src/Assets/Mask group dexter (1).png')")
        self.label.setObjectName("label")
        
        # create Label in frame
        self.label_2 = QLabel(self.frame)
        self.label_2.setGeometry(QRect(150, 350, 180, 60))
        self.label_2.setStyleSheet("font: 75 18pt \"Segoe UI\"; color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_2.setText(str(self.jumlahHewan))
        
        # add the frame to the carousel layout
        self.carouselLayout.setSpacing(5)
        self.carouselLayout.addWidget(self.frame)
        self.carouselLayout.setAlignment(Qt.AlignLeft)
        self.carouselLayout.setSpacing(5)
        self.carouselwidth += 480
        self.carousel.setGeometry(QRect(0, 250, self.carouselwidth, 631))
        self.carousel.setLayout(self.carouselLayout)



    def tambahHewan(self):
        self.hewan = h.Hewan(1, "Kucing", "Kucing", "Daging", 1, "1/1/2019", "Jantan", 10)
        print(self.jumlahHewan)
        self.jumlahHewan += 1
        self.createCard(self.carousel.layout().count()+1)
        print(self.carousel.layout().count())
