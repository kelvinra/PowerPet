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

q4 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (3, 'Miko', 'Cat',4, '2018-01-02', 15, 'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Miko.png')"

q5 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (4, 'Guppy', 'Guppy Fish', 1, '2018-01-10', 1, 'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Guppy.png')"
conn.execute(q2)
conn.execute(q3)
conn.execute(q4)
conn.execute(q5)
conn.commit()
print ("Table created successfully");
conn.close()