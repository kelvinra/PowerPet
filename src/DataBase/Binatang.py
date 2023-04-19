import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem


conn = sqlite3.connect('src/DataBase/Hewan.db')
print ("Opened database successfully")
q1 = '''CREATE TABLE IF NOT EXISTS Hewan
         (ID INT PRIMARY KEY     NOT NULL,
         nama           TEXT    NOT NULL,
         jenis           TEXT    NOT NULL,
         umur            INT     NOT NULL,
         birthdate       TEXT    NOT NULL,
         berat           INT     NOT NULL,
         gender          TEXT   NOT NULL,        
         foto            TEXT    );'''
q2 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,gender,foto) \
       VALUES (1, 'Amara', 'Iguana', 3, '2018-01-02', 10,'betina', 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Amara.png')"
q3 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,gender,foto) \
        VALUES (2, 'Dexter', 'Dog', 5, '2018-01-02', 10,'jantan', 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Dexter.png')"

q4 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,gender,foto) \
        VALUES (3, 'Miko', 'Cat',4, '2018-01-02', 15,'betina', 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Miko.png')"

q5 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,gender,foto) \
        VALUES (4, 'Guppy', 'Guppy Fish', 1, '2018-01-10', 1,'betina', 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Guppy.png')"

q10 = '''CREATE TABLE IF NOT EXISTS Makanan
        (ID INT                      NOT NULL,
        jenisMakanan           TEXT    NOT NULL,
        namaMakanan           TEXT    NOT NULL);'''

q11 = '''CREATE TABLE IF NOT EXISTS Kesehatan
        (ID INT                      NOT NULL,
        CatatanKesehatan           TEXT    NOT NULL,
        periode           TEXT    NOT NULL,
        tanggalPeriksa           TEXT    NOT NULL);'''

q20 = "drop table Hewan"

q21 = "INSERT INTO Makanan (ID,jenisMakanan,namaMakanan) \
        VALUES (3, 'Royal Canin', 'Tuna Fish')"
q22 = "INSERT INTO Makanan (ID,jenisMakanan,namaMakanan) \
        VALUES (4, 'Pelet', 'kecil')"

q23 = "INSERT INTO Makanan (ID,jenisMakanan,namaMakanan) \
        VALUES (2, 'Pro Plan', 'Essentials chicken')"
q24 = "INSERT INTO Makanan (ID,jenisMakanan,namaMakanan) \
        VALUES (1, 'Sayuran', 'Sawi Hijau')"
# conn.execute(q1)
# conn.execute(q2)
# conn.execute(q3)
# conn.execute(q4)
# conn.execute(q5)
# conn.execute(q21)
# conn.execute(q22)
# conn.execute(q23)
# conn.execute(q24)
# conn.commit()
# conn.commit()

j1 = '''CREATE TABLE IF NOT EXISTS Aktivitas
         (ID_Aktivitas INTEGER PRIMARY KEY AUTOINCREMENT,
         ID_Hewan INTEGER NOT NULL,
         nama_aktivitas TEXT NOT NULL,
         tanggal TEXT NOT NULL,
         prioritas INTEGER NOT NULL,
         FOREIGN KEY (ID_Hewan) REFERENCES Hewan(ID));'''
# conn.execute(j1)

j3 = "INSERT INTO Aktivitas (ID_Hewan,nama_aktivitas,tanggal,prioritas) \
        VALUES (1, 'Makan', '2023-01-02', 1)"
j4 = "INSERT INTO Aktivitas (ID_Hewan,nama_aktivitas,tanggal,prioritas) \
        VALUES (1, 'Mandi', '2023-01-03', 2)"
conn.execute(q1)
conn.execute(q2)
conn.execute(q3)
conn.execute(q4)
conn.execute(q5)
# conn.execute(j3)
# conn.execute(j4)
z1 = "Drop table Hewan"
# conn.execute(z1)
conn.commit()
print ("Table created successfully");
conn.close()