import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem


conn = sqlite3.connect('src/DataBase/Hewan.db')
print ("Opened database successfully")
# q1 = '''CREATE TABLE IF NOT EXISTS Hewan
#          (ID INT PRIMARY KEY     NOT NULL,
#          nama           TEXT    NOT NULL,
#          jenis           TEXT    NOT NULL,
#          umur            INT     NOT NULL,
#          birthdate       TEXT    NOT NULL,
#          berat           INT     NOT NULL,
#          foto            TEXT    );'''
# conn.execute(q1)


q2 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
      VALUES (1, 'Amara', 'Iguana', 3, '2018-01-02', 10, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Amara.png')"
q3 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (2, 'Dexter', 'Dog', 5, '2018-01-02', 10, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Dexter.png')"

q4 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (3, 'Miko', 'Cat',4, '2018-01-02', 15, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Miko.png')"

q5 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
        VALUES (4, 'Guppy', 'Guppy Fish', 1, '2018-01-10', 1, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Guppy.png')"

q5 = '''CREATE TABLE IF NOT EXISTS Klinik
        (IDKlinik INT PRIMARY KEY     NOT NULL,
        namaKlinik           TEXT    NOT NULL,
        alamat           TEXT    NOT NULL,
        jamPraktek           TEXT    NOT NULL,
        telepon            TEXT     NOT NULL);'''

# q6 = "INSERT INTO klinik (IDKlinik,namaKlinik,alamat,jamPraktek,telepon) \
#       VALUES \
#       (1, 'VIRGIN PET CARE DENPASAR', 'JL TUKAD PENET NO 25 RENON DENPASAR', '8:30:00 AM', '085737180283'), \
#       (2, 'VIRGIN PET CARE GIANYAR', 'JL BYPASS DARMA GIRI BR SEMA BITERA GIANYAR', '9:20:00 AM', '085737180283'), \
#       (3, 'SHALOM VET', 'PENATARAN SARI 2 NO 7, DENPASAR, BALI', '10:20:00 PM', '081805653087'), \
#       (4, 'Viva Vet', 'Ruko eboni no 21 Taman Royal 3 jl benteng Betawi Poris Cipondoh tangerang', '9:20:00 AM', '087889417529'), \
#       (5, 'Praktek drh yuanita sevryana', 'Jl bima 1 blok e no 27 duta asri 3 Kotabumi Tangerang', '7:10:00 AM', '087871481415'), \
#       (6, 'Klinik Hewan Purnama', 'Jl. Purnama 1 Komplek Purnama Permai 2 No.D12 Pontianak', '8:00:00 AM', '08115771133'), \
#       (7, 'Animalia Petcare', 'Jl. Pahlawan GG 1 (GG pilar) ke timur 700m. Rejoagung kec kedungwaru kab Tulungagung-jatim', '9:00:00 AM', '081334276774'), \
#       (8, 'Me Vet', 'Jl. Kebagusan II, No. 52a, RT. 02/07, Kebagusan, Pasar Minggu, Jak-Sel 12520', '9:21:00 AM', '089676956391'), \
#       (9, 'Kandara Veterinary Care', 'Jln.Raya Kodau No.27C Jatimakmur, Pondok Gede, Bekasi', '10:20:00 AM', '081319235763'), \
#       (10, 'Klinik Hewan Adika', 'JL. KH. Ahmad Dahlan No.52 Keprabon Surakarta', '9:00:00 AM', '081282157575'), \
#       (11, 'ZiZa Vet Clinic& Pet Shop', 'Jl H.A Manap RT 11 RW 04 Depan Prima Tenda Kel. Sungai Kerjan Kec. Bungo Dani Kab. BUNGO', '9:00:00 AM', '085376445125'), \
#       (12, 'King petshop', 'Lingkungan Mendut 3 RT 3 RW 6 Mendut Mungkid magelang', '9:00:00 AM', '085228564644'), \
#       (13, 'Afiyat vetcare and support', 'Jl. Kol ahmad syam no 136 B jatinangor', '10:00:00 AM', '08121427140'), \
#       (14, 'Praktek Dokter Hewan dr. Ul', 'Jln. Tirta Kencana 1 No. 1, RT. 01/02, Kec. Ciputat, Kota Tangerang Selatan, Banten 15412', '9:00:00 AM', '08121111111'), \
#       (15, 'Ocha vet klinik', 'Jl. Kebon Sirih No. 1, RT.1/RW.1, Kebon Sirih, Menteng, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10340', '08.00-17.00', '0213900000'), \
#       (16, 'Zoom Pet Care', 'Jl. Golf Barat Raya No. 22, Arcamanik, Kota Bandung', '9.00.00 AM', '081324600180')"
# q7 = update klinik set namaKlinik = 'Klinik Hewan Momo' where IDKlinik = 15

# select all in klinik
# conn.execute(q2)
# conn.execute(q3)
# conn.execute(q4)
# conn.execute(q5)
conn.execute(q7)




conn.commit()

print ("Table created successfully");


conn.close()