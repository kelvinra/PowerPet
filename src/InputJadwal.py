from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

from PyQt5 import QtWidgets, QtCore, QtGui
import sqlite3 as sql

class InputJadwal(QDialog):
    

    def __init__(self):
        super(InputJadwal, self).__init__()
        loadUi('src/BuilderUI/InputJadwal.ui', self)
        calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        year_button = self.findChild(QtWidgets.QToolButton, "qt_calendar_yearbutton")
        # make year button invisible
        year_button.setVisible(False)

        # Set the text color for every day of the week to black
        day_format = QtGui.QTextCharFormat()
        day_format.setForeground(QtGui.QBrush(QtCore.Qt.black))
        calendar.setWeekdayTextFormat(QtCore.Qt.Sunday, day_format)
        calendar.setWeekdayTextFormat(QtCore.Qt.Saturday, day_format)

        confirm_button = self.findChild(QtWidgets.QPushButton, "confirmInput")

        nama_kegiatan = self.findChild(QtWidgets.QLineEdit, "namaKegiatan")
        prioritas = self.findChild(QtWidgets.QSpinBox, "prioritasBox")

        # connect the confirm button to the on_confirm_clicked function
        confirm_button.clicked.connect(self.on_confirm_clicked)

        selected_date = calendar.selectedDate()

        self.calendar = calendar
        self.selected_date = selected_date
        self.ID_Hewan = 0
        self.nama_kegiatan = nama_kegiatan
        self.prioritas = prioritas

    def idData(self, id):
        self.ID_Hewan = id
    def on_confirm_clicked(self):
        if self.selected_date.toString("yyyy-MM-dd") and self.nama_kegiatan.text():
            self.insert_to_database()
    
    def insert_to_database(self):
        # connect to the database
        con = sql.connect("src/DataBase/Hewan.db")
        cur = con.cursor()
        # insert the data to the database
        calendar = self.findChild(QtWidgets.QCalendarWidget, "calendarWidget")
        selected_date = calendar.selectedDate()

        try:
            cur.execute("INSERT INTO Aktivitas (ID_Hewan, nama_aktivitas, tanggal, prioritas) VALUES (?,?,?,?)", (self.ID_Hewan, self.nama_kegiatan.text(), selected_date.toString("yyyy-MM-dd"), self.prioritas.value()))
            con.commit()
            self.notif_value.setText("Data berhasil dimasukkan")
            self.notif_container.show()
            QtCore.QTimer.singleShot(3000, lambda: self.notif_container.hide())
        except:
            con.rollback()
            self.notif_value.setText("Data gagal dimasukkan")
            self.notif_container.show()
            QtCore.QTimer.singleShot(3000, lambda: self.notif_container.hide())
        con.close()
    
    def show_message_box(self, message):
        msg = QMessageBox()
        #change background of message box
        #make the ok button to center
        #delete the i icon
        msg.setStyleSheet('''
        QMessageBox {
            background-color: rgb(255, 255, 255);
            color: rgb(0, 0, 0);
            border: 1px solid rgb(0, 0, 0);
            border-radius: 5px;
            padding: 5px;
            min-width: 80px;
            min-height: 30px;
        }

        /* change the font size of the message box */
        QMessageBox QLabel {
            font-size: 24px;
            font-family: "Inter";
        }

        /* change the ok button to center */
        QMessageBox QPushButton {
            min-width: 80px;
            min-height: 30px;
            max-width: 80px;
            max-height: 30px;
            border-radius: 5px;
            border: 1px solid rgb(0, 0, 0);
            background-color: rgb(255, 255, 255);
            color: rgb(0, 0, 0);
        }

        QPushButton:hover {
            background-color: #aaffff;
        }
        QPushButton:pressed {
            background-color: #55aaff;
        }

        ''')
        
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Informasi")
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()