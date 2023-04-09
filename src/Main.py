import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/BuilderUI/Main.ui', self)
        self.Logo.clicked.connect(self.openMenu)

    def openMenu(self):
        widget.setCurrentIndex(1)
        


class MenuWindow(QDialog):
    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi('src\BuilderUI\Menu.ui', self)


app = QApplication(sys.argv)
window = MainWindow()
widget = QtWidgets.QStackedWidget()
menu = MenuWindow()
widget.addWidget(window)
widget.addWidget(menu)
widget.setFixedWidth(1920)
widget.setFixedHeight(1024)
widget.show()

sys.exit(app.exec_())
