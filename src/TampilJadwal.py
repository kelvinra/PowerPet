from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor, QFont, QFontMetrics
from PyQt5.QtCore import QDate
import sqlite3 as sql
import datetime

class TampilJadwal(QDialog):
    

    def __init__(self, ID_Hewan):
        self.ID_Hewan = ID_Hewan
        super(TampilJadwal, self).__init__()
        loadUi('src/BuilderUI/TampilJadwal.ui', self)
        calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        year_button = self.findChild(QtWidgets.QToolButton, "qt_calendar_yearbutton")
        # make year button invisible
        year_button.setVisible(False)

        # Set the text color for every day of the week to black
        day_format = QtGui.QTextCharFormat()
        day_format.setForeground(QtGui.QBrush(QtCore.Qt.black))
        calendar.setWeekdayTextFormat(QtCore.Qt.Sunday, day_format)
        calendar.setWeekdayTextFormat(QtCore.Qt.Saturday, day_format)

        # highlight the dates
        self.init_highlight_dates()

        self.cardLayout = self.findChild(QtWidgets.QVBoxLayout, "cardLayout")
        self.cardLayout.setSpacing(20)

        self.container = QtWidgets.QWidget()
        self.container.setStyleSheet("background-color: transparent;")
        self.container.setLayout(self.cardLayout)

        self.scrollArea = self.findChild(QtWidgets.QScrollArea, "scrollArea")
        self.scrollArea.setWidget(self.container)

        # make the cardLayout items always on top
        self.cardLayout.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea = self.findChild(QtWidgets.QScrollArea, "scrollArea")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)

        nextMonthButton = self.findChild(QtWidgets.QToolButton, "qt_calendar_nextmonth")
        nextMonthButton.clicked.connect(self.updateCards)
        prevMonthButton = self.findChild(QtWidgets.QToolButton, "qt_calendar_prevmonth")
        prevMonthButton.clicked.connect(self.updateCards)
        monthButton = self.findChild(QtWidgets.QToolButton, "qt_calendar_monthbutton")
        monthButton.clicked.connect(self.updateCards)

        # make the month button cant be clicked
        monthButton.setEnabled(False)

        addJadwalButton = self.findChild(QtWidgets.QPushButton, "addJadwalButton")
        addJadwalButton.clicked.connect(self.addJadwal)

        self.updateCards()
        
    def init_highlight_dates(self):
        data = self.load_data()
        highlighted_dates = [row[3] for row in data]
        format = QTextCharFormat()
        brush = QBrush(QColor("#FD7F63")) # set the color of the background
        format.setBackground(brush)
        format.setFontWeight(QFont.Bold) # set the font weight to bold
        calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        for date in highlighted_dates:
            dateformat = QDate.fromString(date, "yyyy-MM-dd")
            calendar.setDateTextFormat(dateformat, format)
    
    def load_data(self):
        con = sql.connect("src/DataBase/Hewan.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Aktivitas WHERE ID_Hewan = ?", (self.ID_Hewan,))
        data = cur.fetchall()
        return data
    
    def load_data_by_month(self, month):
        con = sql.connect("src/DataBase/Hewan.db")
        cur = con.cursor()
        # order by date
        cur.execute("SELECT * FROM Aktivitas WHERE ID_Hewan = ? AND strftime('%m', Tanggal) = ? ORDER BY Tanggal ASC, prioritas DESC", (self.ID_Hewan, month))
        data = cur.fetchall()
        return data
    
    def add_card(self, nama_kegiatan, tanggal):
        card = QtWidgets.QWidget()
        # set min max card size
        card.setMinimumSize(493, 86)
        card.setMaximumSize(493, 86)
        card.setStyleSheet("background-color: #FD7F63; border-radius: 20px;")
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        # add shadow to the card
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(4)
        shadow.setXOffset(0)
        shadow.setYOffset(4)
        shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        card.setGraphicsEffect(shadow)

        layout = QtWidgets.QHBoxLayout()

        layout_left = QtWidgets.QVBoxLayout()
        layout_left.setAlignment(QtCore.Qt.AlignTop)
        layout_left.setSpacing(0)

        layout_right = QtWidgets.QVBoxLayout()
        layout_right.setAlignment(QtCore.Qt.AlignTop)
        layout_right.setSpacing(0)

        day = tanggal.split("-")[2]
        day_label = QtWidgets.QLabel(day)
        day_label.setStyleSheet("font-size: 32px; font-family: Inter; font-weight: bold; color: white;")
        day_label.setWordWrap(True)
        day_label.setAlignment(QtCore.Qt.AlignCenter)


        day_of_week = datetime.datetime.strptime(tanggal, "%Y-%m-%d").strftime("%A")
        day_of_week_label = QtWidgets.QLabel(day_of_week)
        day_of_week_label.setStyleSheet("font-size: 16px; font-family: Inter; color: white;")
        day_of_week_label.setWordWrap(True)
        day_of_week_label.setAlignment(QtCore.Qt.AlignCenter)

        nama_kegiatan_label = QtWidgets.QLabel(nama_kegiatan)
        nama_kegiatan_label.setStyleSheet("font-size: 16px; font-family: Inter; color: white;")
        nama_kegiatan_label.setWordWrap(True)

        layout_left.addWidget(day_label, 5)
        layout_left.addWidget(day_of_week_label, 1)

        layout_right.addWidget(nama_kegiatan_label)

        layout_right.setContentsMargins(0, 10, 0, 0)

        layout.addLayout(layout_left, 1)
        layout.addLayout(layout_right, 5)

        card.setLayout(layout)
        
        self.cardLayout.addWidget(card)

    def delete_cards(self):
        for i in reversed(range(self.cardLayout.count())): 
            self.cardLayout.itemAt(i).widget().setParent(None)

    def updateCards(self):
        self.delete_cards()
        calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        month = calendar.monthShown()
        month = str(month).zfill(2)
        data = self.load_data_by_month(month)
        for row in data:
            self.add_card(row[2], row[3])

    def addJadwal(self):
        pass