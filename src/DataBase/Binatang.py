import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem


conn = sqlite3.connect('DataBase/Hewan.db')
print ("Opened database successfully")
q1 = '''CREATE TABLE IF NOT EXISTS Hewan
         (ID INT PRIMARY KEY     NOT NULL,
         nama           TEXT    NOT NULL,
         jenis           TEXT    NOT NULL,
         umur            INT     NOT NULL,
         birthdate       TEXT    NOT NULL,
         berat           INT     NOT NULL,
         gender          TEXT CHECK (gender IN ('jantan', 'betina')),        
         foto            TEXT    );'''
conn.execute(q1)
q2 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,gender,foto) \
      VALUES (1, 'Amara', 'Iguana', 3, '2018-01-02', betina, 10, 'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Amara.png')"
q3 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (2, 'Dexter', 'Dog', 5, '2018-01-02', jantan, 10, 'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Dexter.png')"

q10 = '''CREATE TABLE IF NOT EXISTS Makanan
        (ID INT                      NOT NULL,
        jenisMakanan           TEXT    NOT NULL,
        namaMakanan           TEXT    NOT NULL);'''

q11 = '''CREATE TABLE IF NOT EXISTS Kesehatan
        (ID INT                      NOT NULL,
        CatatanKesehatan           TEXT    NOT NULL,
        periode           TEXT    NOT NULL,
        tanggalPeriksa           TEXT    NOT NULL);'''

conn.execute(q11)
# conn.commit()
print ("Table created successfully");
conn.close()