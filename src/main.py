from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import button as bt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1920, 1080)
        image = QImage("src/Assets/HomeScreen.png")
        sImage = image.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.styleSheet = "background-image: url(/home/kelvin/Documents/rpl/if2250-2023-k03-4-powerpet/src/Assets/HomeScreen.png);"
        self.__initUi()


    def __initUi(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(715, 75, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)
        button = bt.LogoButton()
        layout.addWidget(button)
        widget.setGeometry(700, 100, 700, button.height())
        self.setCentralWidget(widget)
        button.clicked.connect(self.__buttonClicked)

    def __buttonClicked(self):
        # go to menuWindow
        self.menuWindow = MenuWindow()
        self.menuWindow.show()
        self.close()

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1920, 1080)
        image = QImage("src/Assets/Background.png")
        sImage = image.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.__initUi()

    def __initUi(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(715, 75, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)
        button = bt.LogoButton()
        layout.addWidget(button)
        widget.setGeometry(700, 100, 700, button.height())
        self.setCentralWidget(widget)
        button.clicked.connect(self.__buttonClicked)

    def __buttonClicked(self):
        self.close()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()

    sys.exit(app.exec_())
