class Mahasiswa(object):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

c0 = Mahasiswa('Satria', 102, 'Wonogiri', 250000)
c1 = Mahasiswa('Utama', 103, 'Solo', 200000)
c2 = Mahasiswa('Galih', 104, 'Surakarta', 220000)
c3 = Mahasiswa('Edi', 105, 'Surabaya', 230000)
c4 = Mahasiswa('Fahri', 101, 'Karanganyar', 210000)
c5 = Mahasiswa('Tiar', 106, 'Sragen', 260000)


Daftar = [c0, c1, c2, c3, c4, c5]

def urutNIM(a):
    baru = {}
    for i in range(len(a)):
        baru[a[i].nama] = a[i].NIM
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elem in listofTuples:
        print (elem[0], ':', elem[1])

urutNIM(Daftar)
