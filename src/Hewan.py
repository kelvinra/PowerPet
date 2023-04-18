class Hewan:
    def __init__(self, id, nama, jenis, makanan, umur, birthdate, gender, berat):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.makanan = makanan
        self.Umur = umur
        self.birthdate = birthdate
        self.gender = gender
        self.berat = berat

    def setId(self, id):
        self.id = id

    def setNama(self, nama):
        self.nama = nama

    def setJenis(self, jenis):
        self.jenis = jenis

    def setMakanan(self, makanan):
        self.makanan = makanan    
    
    def setUmur(self, Umur):
        self.Umur = Umur
    
    def setBirthdate(self, birthdate):
        self.birthdate = birthdate
    
    def setGender(self, gender):
        self.gender = gender
    
    def setBerat(self, berat):
        self.berat = berat
    
    def getId(self):
        return self.id

    def getNama(self):
        return self.nama
    
    def getJenis(self):
        return self.jenis
    
    def getMakanan(self):
        return self.makanan
    
    def getUmur(self):
        return self.Umur
    
    def getBirthdate(self):
        return self.birthdate
    
    def getGender(self):
        return self.gender
    
    def getBerat(self):
        return self.berat
    

# genderlist = ["jantan", "betina"]
# gender = input(genderlist