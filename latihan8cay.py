# Tugas Dictionary

dictAwal = {}

# Fungsi untuk menampilkan dictionary
def showDictionary():
    print('=================================')
    print('|\tKey\t|\tValue\t|')
    print('=================================')
    for i in (list(dictAwal)):
        if (str(dictAwal[i]).isdigit()==True)  :
            print("|\t'"+ str(i) + "'\t|\t" + str(dictAwal.get(i))+"\t|")
        else:
            print("|\t'"+ str(i) + "'\t|\t'" + str(dictAwal.get(i))+"'\t|")
    print('=================================')

# Fungsi untuk menambahkan dictionary
def addDictionary():
    inputDict= input('Masukan jumlah dictionary yang akan diinput= ')
    for i in range (int(inputDict)):
        inputKey= input('Masukan nama key ke-'+ str(i+1) + ' yang diinginkan= ')
        valueType= input('Jenis value yang akan diinput\n1. string\n2. integer\nPilih 1/2= ')
        inputValue= input('Masukan value dari key '+ inputKey +' = ')
        if int(valueType) == 1:
            dictAwal[inputKey]=inputValue
        elif int(valueType) == 2:
            dictAwal[inputKey]=int(inputValue)
    print('Data sudah berhasil diinputkan ')
    return dictAwal

# Fungsi untuk mencari dan filter dictionary
def searchDictionary():
    print(dictAwal)
    b = input ('Search : ')
    newList=filter(lambda c : b.lower() in str.lower(c), dictAwal)
    newDict={}
    for i in (list(newList)):
        newDict[i]=dictAwal.get(i)
    print('=================================')
    print('|\tKey\t|\tValue\t|')
    print('=================================')
    for i in (list(newDict)):
        print('|\t'+ str(i) + '\t|\t'+ str(newDict.get(i))+'\t|')
    print('=================================')

# Aplikasi utama
keluar = False
while keluar==False:
    print('Main menu\n1. Lihat full dictionary\n2. Isi Dictionary\n3. Searching Dictionary\n4. Keluar')
    pilihMenu = input('Pilih 1/2/3/4 = ')
    menu = [showDictionary, addDictionary, searchDictionary]
    if int(pilihMenu)<4:
        menu[int(pilihMenu)-1]()
        ask= input('Apakah anda ingin\n1. Keluar\n2. Kembali ke menu awal\nPilih1/2= ')
        if int(ask)==1:
            break
    elif int(pilihMenu)==4:
        keluar = True
print('Terimakasih sudah menggunakan aplikasi kami')

# Delete dictionary (ex: satu elemen) bisa menggunakan del dict['key]





