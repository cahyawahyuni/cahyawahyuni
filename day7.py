# Dictionaries (mirip kaya list, tapi beda dari segi index)

# #contoh 1
# nama = {'depan':'Cahya', 'belakang':'Wahyuni'}
# print(nama['depan']) # Hasilnya Cahya, mainnya di unique keynya (depan/belakang). unique key gaboleh sama, kalau sama dia bakal nimpa nilai yang sebelumnya)
# #contoh 2
# d = { "key1" : "item1", "key2" : "item2", "kucing" : [3, "jerapah"] }
# print(d["key1"])
# print(d["key2"])
# print(d["kucing"]) #dapatnya list kucing
# print(d["kucing"][1]) #dapatnya nilai list kucing index 1
# # contoh matrix list 2D
# produk = [ 
#     ['Jeruk',2000], 
#     ['Apel',3000], 
#     ['Anggur',4000]
#     ] #list 2 dimensi, di dalam list nilainya masih list juga

# # print(produk[2][1]) #untuk dapatkan harga anggur
# cart = [
#     [0,3],
#     [2,5],
#     [1,4]
# ]

# out=''
# i=0
# while (i<len(produk)):
#     out += (str(i+1) + '. ' + produk[i][0] + ' Rp. ' + str(produk[i][1])+'\n')
#     i+=1
# print(out) 

# hasil=''
# for i in range (len(cart)):
#     hasil+=(produk[cart[i][0]][0] +' Rp.' + str(produk[cart[i][0]][1]) + ' x ' + str(cart[i][1])+ ', Total Harga = Rp.' + str((produk[cart[i][0]][1])*(cart[i][1]))+'\n')
# print(hasil)

# TUPLES, mirip list tapi isinya gak bisa diubah, kecuali isi di tuplesnya list/ dictionary (list/dictionarynya yg bisa diedit)
# t = (1, [0, "test"], { "a1" : True })
# print(t[2]["a1"]) 
# print(t[1][1])
# t[1][1] = "akan" # bisa karena yang diedit list
# print(t[1][1]) 
# # t[1] = "mark" #gak bisa karena mau edit yang tuflesnya
# print(t[1])

#Tuples inside tuples (method pythonnya ga banyak, cuma count dan index saja, search w3schools.com/python for detail)
# t = (1, [0, "test"], { "a1" : True }, (0,{ "test" : 5 },2))
# print(t[3][1]["test"]) #hasilnya 5

# Sets (gak support indexing, every item unique)
# abc = {3,2,4,5,1,2}
# print(abc) #hasil {1,2,3,4,5} bentuknya masih set masih kurung kurawal dan keluar hasil yg unik aja
# # kalau ambil print(abc[0]) akan eror karena gak support indexing
# # maka ubah dulu jadi list kalau mau diambil indexnya
# print(list(abc)) #hasil [1,2,3,4,5] udah jadi list pakai kurung [], udah bisa di index
# print(list(abc)[1])

# # Filtering List Using Set (ambil unique valuenya aja, penempatannya ngacak)
# newList = [ 1, 3, "test1", "test2" , 2, 3, "test1" ]
# s = set(newList)
# print(s)
# print(list(s)[2])

# # List Comprehension
# listNum = [ 1, 2, 3, 4, 5, 'ayam']
# listNum = [item * 2 for item in listNum]
# print(listNum)
# dengan list comprehension
# newlist = ['a','b','c','d']
# list2=[i + ' purwadhika' for i in newlist]
# print(list2)
# # tanpa list Comprehension
# list2 =[]
# for item in newlist:
#     list2.append(item+' purwadhika')
# print(list2)

# nested loop tanpa list comprehension
# test=[]
# for i in range(1,3):
#     seg=''
#     for j in range (2):
#         test.append(j)
# print(test)
# # nested loop dengan list comprehension
# tes2=[j for i in range(1,3) for j in range(2)]
# print(tes2)

# # Lambda Expressions (small anonymous function)
# x = lambda a : a +10
# print(x(5))
# bila pakai fungsi
# def times2(num) : 
#     return num * 2
# print(times2(5))
# bila pakai lambda
# y=lambda num: num * 2
# print(y(5))

# # Map 
# Tanpa Lambda (menggunakan function)
# def times2(num) : 
#     return num * 2
# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(times2, listNum)) # syntax map(funct, iterables)
# print(listNum)

# Menggunakan Lambda
# listNum = [1,2,3,4,5]
# listNum = list(map(lambda num:num*2,listNum))
# print(listNum)

# Contoh lain menggunakan fungsi
# def umur(tahunLahir):
#     return 2019-tahunLahir
# tahun = [1990,1978,1980,1992]
# # # gunakan map
# # listUmur = map(umur,tahun)
# # print(list(listUmur))

# # manual tanpa map (cek github ulang)
# def dupMap(fn , listAja):
#     newList = []
#     for item in listAja :
#         newList.append(fn(item))
#     return newList

# listumur = dupMap(umur,tahun)
# print(listumur)


# Filter bakal print yang true
tahun =[1990,1945,1977,1978,1980,1992]
newList = filter(lambda tahun:tahun % 2 == 0, tahun)
print(list(newList))

# Tugas
# 1 bikin duplikat filter
# 2 Method for searching
    # numlist = [2,3,4,1,10]
    #  print(11 in numlist) => akan hasilkan false, bila 10 in numlist bernilai true




