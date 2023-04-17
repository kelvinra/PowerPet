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


# q2 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#       VALUES (1, 'Amara', 'Iguana', 3, '2018-01-02', 10, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Amara.png')"
# q3 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#         VALUES (2, 'Dexter', 'Dog', 5, '2018-01-02', 10, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Dexter.png')"

# q4 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#         VALUES (3, 'Miko', 'Cat',4, '2018-01-02', 15, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Miko.png')"

# q5 = "INSERT INTO Hewan (ID,nama,jenis,umur,birthdate,berat,foto) \
#         VALUES (4, 'Guppy', 'Guppy Fish', 1, '2018-01-10', 1, 'D:\Kelvin\code\semester 4\RPL\if2250-2023-k03-4-powerpet\src\Assets\Guppy.png')"

q5 = '''CREATE TABLE IF NOT EXISTS Klinik
        (IDKlinik INT PRIMARY KEY     NOT NULL,
        namaKlinik           TEXT    NOT NULL,
        alamat           TEXT    NOT NULL,
        jamPraktek           TEXT    NOT NULL,
        telepon            TEXT     NOT NULL);'''

# q8 = "INSERT INTO klinik (IDKlinik,namaKlinik,alamat,jamPraktek,telepon) \
#       VALUES \
#       (1, 'Virgin Pet Care Denpasar', 'Jl. Tukad Penet No.25 Renon Denpasar', '8:30:00 AM', '085737180283'), \
#       (2, 'Virgin Pet Care Gianyar', 'Jl. Bypass Darma Giri, Gianyar', '9:20:00 AM', '085737180283'), \
#       (3, 'Shalom Vet', 'Penataran Sari 2 No.7, Denpasar, Bali', '10:20:00 PM', '081805653087'), \
#       (4, 'Viva Vet', 'Jl. Benteng Betawi Poris Cipondoh Tangerang', '9:20:00 AM', '087889417529'), \
#       (5, 'Praktek drh yuanita sevryana', 'Jl. Bima 1 Blok E No.27, Kotabumi Tangerang', '7:10:00 AM', '087871481415'), \
#       (6, 'Klinik Hewan Purnama', 'Jl. Purnama 1 No.D12 Pontianak', '8:00:00 AM', '08115771133'), \
#       (7, 'Animalia Petcare', 'Jl. Pahlawan GG 1,Tulungagung, Jawa Timur', '9:00:00 AM', '081334276774'), \
#       (8, 'Me Vet', 'Jl. Kebagusan II, No.52a, Pasar Minggu, Jakarta Selatan', '9:21:00 AM', '089676956391'), \
#       (9, 'Kandara Veterinary Care', 'Jl. Raya Kodau No.27C, Pondok Gede, Bekasi', '10:20:00 AM', '081319235763'), \
#       (10, 'Klinik Hewan Adika', 'JL. KH. Ahmad Dahlan No.52 Keprabon Surakarta', '9:00:00 AM', '081282157575'), \
#       (11, 'ZiZa Vet Clinic& Pet Shop', 'Jl H.A Manap Kec. Bungo Dani Kab. Bungo', '9:00:00 AM', '085376445125'), \
#       (12, 'King petshop', 'Lingkungan Mendut 3 RT 3 RW 6, Magelang', '9:00:00 AM', '085228564644'), \
#       (13, 'Afiyat vetcare and support', 'Jl. Kol ASyam No.136 B Jatinangor', '10:00:00 AM', '08121427140'), \
#       (14, 'Praktek Dokter Hewan dr. Ul', 'Jl. Tirta Kencana 1 No.1, Tangerang Selatan, Banten', '9:00:00 AM', '08121111111'), \
#       (15, 'Klinik Hewan Momo', 'Jl. kencana II No.19, Palangkaraya, Kalimantan Tengah', '8.00.00 AM', '08115202089'), \
#       (16, 'Zoom Pet Care', 'Jl. Golf Barat Raya No.22, Arcamanik, Kota Bandung', '9.00.00 AM', '081324600180'), \
#       (17, 'Klinik Hewan JF Veteriner','Jl. Bandara SMB II Komplek PDK D-14. Palembang', '9.00.00 AM', '08127882877'), \
#       (18, 'Cita Vet', 'Jl. Sei Besitang No.39, Medan', '4.00.00 PM', '081260124488'), \
#       (19, 'Eldora Vet Clinic', 'Jl. Krakatau No.251 Simpang Empat Bilal, Medan', '8.30.00 AM', '085277429925'), \
#       (20, ' Prima Pet Clinic', 'Jl. Yos Sudarso 85 Batu Ampar, Batam', '9.00.00 AM', '085668401619'), \
#       (21, 'Stella Pet Clinic', 'Jl. Bangbarung raya No.6 Bantarjati, Bogor', '11.00.00 AM', '(0251) 8319038'), \
#       (22, 'Klinik Hewan Makassar', 'Jl. Monumen Emmy Saelan No.103A, Makassar', '9.00.00 AM', '081944255777'), \
#       (23, ' Klinik Hewan Suropati', 'Jl. Suropati No.108, Batu. Malang', '8.00.00 AM', '(0341) 594369')"
# conn.execute(q2)
# conn.execute(q3)
# conn.execute(q4)

q10 = '''CREATE TABLE IF NOT EXISTS Makanan
        (ID INT                      NOT NULL,
        jenisMakanan           TEXT    NOT NULL,
        namaMakanan           TEXT    NOT NULL);'''

q11 = '''CREATE TABLE IF NOT EXISTS Kesehatan
        (ID INT                      NOT NULL,
        CatatanKesehatan           TEXT    NOT NULL,
        periode           TEXT    NOT NULL,
        tanggalPeriksa           TEXT    NOT NULL);'''

q12 = "INSERT INTO Makanan (ID,jenisMakanan,namaMakanan) \
        VALUES \
        (2, 'Pro Plan', 'Essentials Chicken')"
conn.execute(q12)
conn.commit()
print ("Table created successfully");
conn.close()