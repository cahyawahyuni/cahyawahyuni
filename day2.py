# KOMENTAR YANG TIDAK AKAN TERBACA SEBAGAI BAHASA PEMOGRAMAN

# !VARIABLE!
# WADAH UNTUK MENYIMPAN VALUE
# nama = 'cahya'
# ubah variable jadi yang akan kedetect yang terbaru
# nama = 10
# print(nama)

# tipe data
# a = "mawar" # string
# b = 8900 # integer
# c = True # boolean
# d = 3.456 # float

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# !Operator Matematika!
# Penggunaan Operator Hanya bisa untuk jenis data yang sama
# import math
# angka1 = 5
# angka2 = 10
# angka3 = '15'
# angka4 = '20'
# print(angka1+angka2) #15
# print(angka3+angka4) #1520
# print(angka1+ int(angka3)) #eror kalau tanpa int karena data beda, hasilnya 20
# print(angka1*angka3) #1515151515
# print(int(angka4)%3) #eror kalau tanpa int, hasilnya 2
# print(angka2/angka1)
# print (5/2)
# print(round(5/2))

# !control flow / pengkondisian!
# && operator comparison
# = == === >= <= > <
# penggunaan if sensitif untuk spasinya, jadi harus disesuaikan
# a = 5
# if(a>4):
#     print("Good")
# else:
#     print('Bad')

# a=5
# b=10
# a=20
# if(a - b == 10):
#     print('good')
#     if(a>5):
#         print("great")
#     else:
#         print('damn')
# else:
#     print("bad")

# else if
# c=5
# if(c<4):
#     print('good')
# elif(c>6):
#     print('great')
# elif(c>9):
#     print('perfect')
# else:
#     print('default')

# !Input process output!
# angka = input ('Masukan Angka :') # input selalu menghasilkan string
# print('Anda Menginput Angka ' + angka)
#data dari input pasti string

# nama = input ('nama = ')
# umur = input ('tahun lahir = ')
# umur = 2019 - int(umur)
# pekerjaan = input ('pekerjaan = ')
# # print('Masukan nama = ' + nama)
# # print('Masukan umur = ' + str(umur))
# # print('Masukan pekerjaan'+ pekerjaan) 
# print(nama + ' berumur '+ str(umur) +' tahun, Dia adalah '+ pekerjaan)

# angka1 = input ('masukan angka pertama : ')
# angka1 = int(angka1)
# angka2 = input ('masukan angka kedua : ')
# angka2 = int(angka2)
# operator = input ('pilih operator (+,-,/) : ')
# if(operator=='+'):
#     print(angka1+angka2)
# elif(operator=='-'):
#     print(angka1-angka2)
# elif(operator=='/'):
#     print(angka1/angka2)

# !Tugas APLIKASI PARKIR SEDERHANA!
# input = Jam berapa masuk parkiran? 1-12
#          Pagi atau malam?
#          Jam Berapa keluar parkiran? 1-12
#          Pagi atau malam?
# Output = Anda parkir selama ... jam, anda harus bayar ...
# Harga 3 Jam pertama 3000/jam
#   setelah 3 jam pertama 1000/jam
#   maksimal 25000
# kirim .py ke jamaludinfikrii@gmail.com sebelum jam 08.00

# !import math!
# print(round(4.7)) #round otomatis ke atas >0.5
# print(round(4.4)) #round otomatis ke bawah <0.5
# print(math.floor(4.7)) #bulatin ke bawah terdekat
# print(math.ceil(4.4)) #bulatin ke atas terdekat
# print(math.pi) #keluarin nilai pi
# print(math.fabs(-4.7)) #hasilkan nilai absolut
# print(math.pow(8,2)) #pangkat (8^2)
# print(math.sqrt(64)) #akar

# !Strings!
# x = 'Halo Dunia'
# print(len(x)) #panjang karakter x
# print(x.index('Dunia')) #panjang index 'Dunia'
# print(x.split(' ')) #split x berdasarkan 'spasi'
# print(x.lower()) #jadikan huruf kecil semua
# print(x.upper()) #jadikan huruf besar semua
# print(x.capitalize()) #huruf besar di awal

# #penggunaan "" atau '' sama aja, kondisiin aja kalau ada perlu pakai ' di kalimat maka pakai yg ""
# singleQuotes = 'single quotes'
# doubleQuotes = "double quotes"
# combineQuotes = "wrap lot's of other quotes"
# print(singleQuotes)
# print(doubleQuotes)
# print(combineQuotes)

#string indexing (hitungan char awal dari 0)
#a:b = start dari a, berhenti sebelum b
# text = "i.m baron, nice to meet you"
# print(text[1])
# print(text[2:])
# print(text[:4])
# print(text[2:5])
# print(text[:])
# print(text[4:9])

#convert strings to numbers
# angka1 = input('masukan angka = ')
# angka2 = input('masukan angka = ')
# print(angka1+angka2) #jumlahin string
# print(int(angka1)+int(angka2)) #jumlahin int dengan string diubah dulu ke integer
# angka1=float(angka1) #ubah data ke float
# angka2=float(angka2) #ubah data ke float
# print(angka1+angka2) #jumlahin data float

#!Latihan
# import math
# x=4
# y=3
# z=2
# w = math.pow(((x+y*z)/(x*y)),2)
# print(w)

# a=485
# b= a//360
# c=(a-360)//30
# print('485 hari sama dengan ' + str(b) + ' tahun ' + str(c) + " bulan ")

#!Loop!
# angka = input ('masukan angka = ')
# angka = int(angka)
# while(angka <=10):
#     print(angka)
#     angka +=1

#angka yang ke 3 maksutnya longkap2
# listItem = list(range(1,11,2))
# print(listItem)
# for item in range (1,11,2):
#     print(item)

# Latihan
# Angka = 1
# while(Angka<=10):
#     print('Nomor Urut '+ str(Angka))
#     Angka +=1