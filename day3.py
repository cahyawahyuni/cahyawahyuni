# ASSIGNMENT OPERATOR
# a=5
# b=a
# # print(b) #hasil = 5

# b+=a # sama kaya b= b+a, bisa string juga (kalau string di concate)
# print(b) #hasil = 10
# Latihan Solve 2
# import math
# massa = int(input('Masukan massa badan(kg) = '))
# tinggi = (int(input('Masukan tinggi badan(cm) = ')))/100
# imt = massa/(math.pow((tinggi),2))
# if imt<18.5:
#     berat = 'KURANG'
# elif 18.5<=imt<25: #bisa juga (imt >= 18.5 and imt < 25)
#     berat = 'IDEAL'
# elif 25<=imt<30:
#     berat = 'BERLEBIH'
# elif 30<=imt<40:
#     berat = 'SANGAT BERLEBIH'
# elif imt>=40:
#     berat = 'OBESITAS'
# print('Massa ' + str(massa) + ' kg & tinggi ' + str(tinggi) + ' m ')
# print('IMT = ' + str(imt) + ', BERAT BADAN ' + berat)

#!LOOPING! Perpanjangan dari IF
# Jika If kondisi true makan akan jalan sekali
# Jika while kondisi true dia akan jalan terus (looping)
# angka = 1
# while(angka<5): #infinite loop kalau masukin angka > 0 (makannya harus dibikin exit way/ kondisi dimana dia bernilai false)
#     print(angka)
#     angka+= 1

# jumlah = 0
# angka = 1
# while (angka<5):
#     jumlah += angka
#     angka += 1
# print(jumlah) #print ini terakhir ketika loopin udah berhenti, jadi yang keluar hanya hasil dari jumlah yang terakhir

#agar tidak infinite loop bisa pakai break
# angka = 10
# jumlah = 0
# while (angka>0):
#     jumlah += angka
#     angka += 1
#     if(angka == 11):
#         break
# print(jumlah)

# i=10
# out=' '
# while(i>0):
#     out+=str(i)
#     if(i==1):
#         break
#     out += ','
#     i-=1
# print(out)
