##Program Akun
##Dibuat oleh M. Iqbal Rachmad Anwar  L200194074

import random
angka = random.randint(0,1000)

Nama = 'Muhammad Iqbal Rachmad Anwar'
print(Nama)
TanggalLahir = '29 Agustus 2000'
print(TanggalLahir)
NamaSingkat = Nama[0]+'. '+Nama[9:14]+' '+Nama[15]+'. '+Nama[23]
print(NamaSingkat)
Username = Nama[0]+TanggalLahir[:2]+TanggalLahir[11:15]
print(Username)
Password = Nama[0:3]+str(angka)
print(Password)
