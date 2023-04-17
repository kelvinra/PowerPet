import sqlite3

conn = sqlite3.connect('src/DataBase/Hewan.db')
print ("Opened database successfully")
q1 = '''CREATE TABLE IF NOT EXISTS Hewan
         (ID INT PRIMARY KEY     NOT NULL,
         nama           TEXT    NOT NULL,
         jenis           TEXT    NOT NULL,
         umur            INT     NOT NULL,
         birthdate       TEXT    NOT NULL,
         berat           INT     NOT NULL,
         foto            TEXT    );'''
conn.execute(q1)
q2 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
      VALUES (1, 'Amara', 'Iguana', 3, '2018-01-02', 10, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Amara.png')"
q3 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (2, 'Dexter', 'Dog', 5, '2018-01-02', 10, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Dexter.png')"

q4 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (3, 'Miko', 'Cat',4, '2018-01-02', 15, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Miko.png')"

q5 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (4, 'Guppy', 'Guppy Fish', 1, '2018-01-10', 1, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Guppy.png')"
# conn.execute(q2)
# conn.execute(q3)
# conn.execute(q4)
# conn.execute(q5)
# conn.commit()

j1 = '''CREATE TABLE IF NOT EXISTS Aktivitas
         (ID_Aktivitas INTEGER PRIMARY KEY AUTOINCREMENT,
         ID_Hewan INTEGER NOT NULL,
         nama_aktivitas TEXT NOT NULL,
         tanggal TEXT NOT NULL,
         prioritas INTEGER NOT NULL,
         FOREIGN KEY (ID_Hewan) REFERENCES Hewan(ID));'''
conn.execute(j1)

j3 = "INSERT INTO Aktivitas (ID_Hewan,nama_aktivitas,tanggal,prioritas) \
        VALUES (1, 'Makan', '2023-01-02', 1)"
j4 = "INSERT INTO Aktivitas (ID_Hewan,nama_aktivitas,tanggal,prioritas) \
        VALUES (1, 'Mandi', '2023-01-03', 2)"
# conn.execute(j2)
conn.execute(j3)
conn.execute(j4)
print ("Table created successfully");

conn.close()