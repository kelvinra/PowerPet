from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class LogoButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setText("PowerPet")
        QFontDatabase.addApplicationFont("/home/kelvin/Documents/rpl/if2250-2023-k03-4-powerpet/src/Assets/JockeyOne-Regular.ttf")
        self.setFixedSize(470, 150)
        font = QFont("Jockey One", 90)
        self.setFont(font)
        
        # set pos button
        self.move(300, 700) 
        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.valueChanged.connect(self.__setOpacity)
        self.__animation.setStartValue(0.0)
        self.__animation.setEndValue(0.5)
        self.__animation.setDuration(900)
        self.__styleInit(0.0)

    def __styleInit(self, opacity: float):
        style = f'QPushButton {{ background-color: rgb(156, 235, 252, {opacity});' \
                f'border: 0;' \
                f'color: rgb(6, 60, 153);' \
                f'padding: 5;' \
                f'border-radius: 10; }}'
        self.setStyleSheet(style)

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def __setOpacity(self, opacity):
        self.__styleInit(opacity)


class AddHButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setText("Tambah Hewan")
        QFontDatabase.addApplicationFont("/home/kelvin/Documents/rpl/if2250-2023-k03-4-powerpet/src/Assets/JockeyOne-Regular.ttf")
        self.setFixedSize(182, 40)
        font = QFont("Inter", 10)
        self.setFont(font)
        # set pos button
        self.setStyleSheet("background-color: rgb(243, 103, 72, 0.85);")
        self.move(300, 700) 
        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.valueChanged.connect(self.__setOpacity)
        self.__animation.setStartValue(0.85)
        self.__animation.setEndValue(1.0)
        self.__animation.setDuration(200)
        self.__styleInit(0.85)

    def __styleInit(self, opacity: float):
        style = f'QPushButton {{ background-color: rgb(243, 103, 72, {opacity});' \
                f'border: 0;' \
                f'color: rgb(255, 255, 255);' \
                f'padding: 5;' \
                f'border-radius: 20px; }}'
        self.setStyleSheet(style)

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def __setOpacity(self, opacity):
        self.__styleInit(opacity)

class DetailButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setText("Lihat Detail")
        QFontDatabase.addApplicationFont("/home/kelvin/Documents/rpl/if2250-2023-k03-4-powerpet/src/Assets/JockeyOne-Regular.ttf")
        self.setFixedSize(182, 40)
        font = QFont("Inter", 12)
        self.setFont(font)
        # set pos button
        self.setStyleSheet("background-color: rgb(113, 219, 242, 0.5);")
        self.move(300, 700) 
        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.valueChanged.connect(self.__setOpacity)
        self.__animation.setStartValue(0.5)
        self.__animation.setEndValue(1.0)
        self.__animation.setDuration(200)
        self.__styleInit(0.5)

    def __styleInit(self, opacity: float):
        style = f'QPushButton {{ background-color: rgb(113, 219, 242, {opacity});' \
                f'border: 0;' \
                f'color: rgb(6, 60, 153);' \
                f'padding: 5;' \
                f'border-radius: 20px; }}'
        self.setStyleSheet(style)

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def __setOpacity(self, opacity):
        self.__styleInit(opacity)


class ArrowButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setText("<")
        #set text allign center
        
        QFontDatabase.addApplicationFont("/home/kelvin/Documents/rpl/if2250-2023-k03-4-powerpet/src/Assets/JockeyOne-Regular.ttf")
        self.setFixedSize(80, 80)
        font = QFont("Inter", 30)
        self.setFont(font)
        # set pos button
        self.setStyleSheet("background-color: rgb(119, 225, 248, 0.7);")
        self.move(300, 700) 
        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.valueChanged.connect(self.__setOpacity)
        self.__animation.setStartValue(0.7)
        self.__animation.setEndValue(1.0)
        self.__animation.setDuration(200)
        self.__styleInit(0.7)

    def __styleInit(self, opacity: float):
        style = f'QPushButton {{ background-color: rgb(113, 219, 242, {opacity});' \
                f'border: 0 ;' \
                f'color: rgb(255, 255, 255);' \
                f'padding: 5;' \
                f'border-radius: 35px; }}'
        self.setStyleSheet(style)

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)

    def __setOpacity(self, opacity):
        self.__styleInit(opacity)