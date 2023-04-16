from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

class InfoWindow(QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        loadUi('src/BuilderUI/Info.ui', self)

    # def showInfo() :
    #     cursor = Binatang.conn.cursor()
    #     cursor.execute("SELECT * FROM Hewan")
    #     data = cursor.fetchall()
    #     return data



    # def infoInput(idHewan):
    #     cursor = Binatang.conn.cursor()
    #     cursor.execute("SELECT * FROM Hewan WHERE id = ? ", (idHewan,))
    #     data = cursor.fetchone()
    #     if data:
    #         print(data)
    #         return data
    #     else:
    #         print("Hewan dengan ID tersebut tidak ditemukan.")
    #         return None

    # def inputInfo () :
    #     # minta pengguna memasukkan nilai argumen
    #     id = input("Masukkan ID hewan: ")
    #     nama = input("Masukkan nama hewan: ")
    #     jenis = input("Masukkan jenis hewan: ")
    #     makanan = input("Masukkan makanan hewan: ")
    #     umur = input("Masukkan umur hewan: ")
    #     birthdate = input("Masukkan tanggal lahir hewan: ")
    #     gender = input("Masukkan jenis kelamin hewan: ")
    #     berat = input("Masukkan berat hewan: ")
    #     hewan = Hewan(id, nama, jenis, makanan, umur, birthdate, gender, berat)
    #     print (hewan)





