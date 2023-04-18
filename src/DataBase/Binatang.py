import sqlite3
import os 

dirNow = os.path.dirname(os.path.abspath(__file__))
amaraPng = os.path.join(dirNow, '..', 'Assets', 'Amara.png')

conn = sqlite3.connect('src/DataBase/Hewan.db')
print ("Opened database successfully")
# q1 = '''CREATE TABLE IF NOT EXISTS Hewan
#          (ID INT PRIMARY KEY     NOT NULL,
#          nama           TEXT    NOT NULL,
#          jenis           TEXT    NOT NULL,
#          umur            INT     NOT NULL,
#          birthdate       TEXT    NOT NULL,
#          berat           INT     NOT NULL,
#          gender          TEXT CHECK (gender IN ('jantan', 'betina')),        
#          foto            TEXT    );'''
# conn.execute(q1)


# q2 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#       VALUES (1, 'Amara', 'Iguana', 3, '2018-01-02', 10, 'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Amara.png')"

# q3 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#         VALUES (2, 'Dexter', 'Dog', 5, '2018-01-02', 10, 'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Dexter.png')"

# q4 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#         VALUES (3, 'Miko', 'Cat',4, '2018-01-02', 15,  'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Miko.png')"

# q5 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#         VALUES (4, 'Guppy', 'Guppy Fish', 1, '2018-01-10',  1, 'D:\ravu\if2250-2023-k03-4-powerpet\src\Assets\Guppy.png')"

# q6 = "INSERT OR REPLACE INTO Hewan (ID, nama,jenis,umur,birthdate,berat,gender,foto) \
#       VALUES (1, 'Amara', 'Iguana', 3, '2018-01-02', 10, amaraPng)"
# q7 = "INSERT OR REPLACE INTO Hewan (ID, nama,jenis,umur,birthdate,berat,gender,foto) \
#         VALUES (2, 'Dexter', 'Dog', 5, '2018-01-02', 10, 'jantan', '..\Assets\\Dexter.png')"
# q8 = "INSERT OR REPLACE INTO Hewan (ID,nama,jenis,umur,birthdate,berat,gender,foto) \
#         VALUES (3, 'Miko', 'Cat',4, '2018-01-02', 15, 'jantan', '..\\Assets\\Miko.png')"
# q9 = "INSERT OR REPLACE INTO Hewan (ID, nama,jenis,umur,birthdate,berat,gender,foto) \
#         VALUES (4, 'Guppy', 'Guppy Fish', 1, '2018-01-10',  1, '..\\Assets\\Guppy.png')"


# q10 = '''CREATE TABLE IF NOT EXISTS Klinik
#         (IDKlinik INT PRIMARY KEY     NOT NULL,
#         namaKlinik           TEXT    NOT NULL,
#         alamat           TEXT    NOT NULL,
#         jamPraktek           TEXT    NOT NULL,
#         telepon            TEXT     NOT NULL);'''

# q11 = '''CREATE TABLE IF NOT EXISTS Makanan
#         (ID INT                      NOT NULL,
#         jenisMakanan           TEXT    NOT NULL,
#         namaMakanan           TEXT    NOT NULL);'''


# q12 = '''CREATE TABLE IF NOT EXISTS Kesehatan
#         (ID INT                      NOT NULL,
#         CatatanKesehatan           TEXT    NOT NULL,
#         periode           TEXT    NOT NULL,
#         tanggalPeriksa           TEXT    NOT NULL);'''

# conn.execute(q2)
# conn.execute(q3)
# conn.execute(q4)
# conn.execute(q5)
# conn.execute(q6)
# conn.execute(q7)
# conn.execute(q8)
# conn.execute(q9)
# conn.execute(q10)
# conn.execute(q11)
# conn.execute(q12)

conn.commit()

print ("Table created successfully");

conn.close()