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
        self.__animation.setDuration(200)
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
        self.setFixedSize(300,70)
        font = QFont("Jockey One", 40)
        self.setFont(font)
        # set pos button
        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.valueChanged.connect(self.__setOpacity)
        self.__animation.setStartValue(0.0)
        self.__animation.setEndValue(0.5)
        self.__animation.setDuration(200)
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