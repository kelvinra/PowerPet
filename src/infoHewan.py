import Hewan
from DataBase import Binatang
from MenuWindow import createCard

def showInfo() :
    cursor = Binatang.conn.cursor()
    cursor.execute("SELECT * FROM Hewan")
    data = cursor.fetchall()
    return data



def infoInput(idHewan):
    cursor = Binatang.conn.cursor()
    cursor.execute("SELECT * FROM Hewan WHERE id = ? ", (idHewan,))
    data = cursor.fetchone()
    if data:
        print(data)
        return data
    else:
        print("Hewan dengan ID tersebut tidak ditemukan.")
        return None


