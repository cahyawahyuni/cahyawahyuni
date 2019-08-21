# !FOR LOOP!
#range bisa untuk nentuin mau berapa kali looping

# for item in range (1,10): #range(start,stop,step)
#     print(item) #bakal print turun ke bawah
# print(list(range(1,10))) #bakal print jadi list ke samping

#yang sejenis dengan for item in range (1,10)
# item=0
# while(item<10):
#     print(item)
#     item+=1

#Loop Drawing
# z=''
# for item in range(0,5):
#     z+= ' * '
# print(z)

#Nested Loop (looping dalam loop)
# output =''
# for i in range(5):
#     for j in range(5):
#         output += '*'
#     output+='\n' #untuk new line/enter
# print(output)
#VERSI WHILENYA
# i=0
# output=''
# while(i<5):
#     j=0
#     while(j<5):
#         output+='*'
#         j+=1
#     output+="\n"
#     i+=1
# print(output)

# i=0
# out=''
# while(i<3):
#     j=0
#     while(j<4):
#         out += str(j+1)
#         j+=1
#     out+='\n'
#     i+=1
# print(out)    

# output =''
# for i in range(3):
#     for j in range(4):
#         output += str(j+1)
#     output+='\n' 
# print(output)

# i=0
# out=''
# while(i<3):
#     j=0
#     while(j<=i):
#         out += str(j+1)
#         j+=1
#     out+='\n'
#     i+=1
# print(out)

#For Loop Drawing
# out=''
# for i in range(5):
#     for j in range(i+1):
#         out+='*'
#     out+='\n'
# print(out)

# i=0
# out=''
# while(i<5):
#     j=0
#     while(j<5-i):
#         out += '*'
#         j+=1
#     out+='\n'
#     i+=1
# print(out)

# Tugas:
# Mau Bikin Apa ? 1. Segitia siku2 2. segitiga sama kaki 3. persegi
    # 1. ditanya : 1. siku atas 2. siku bawah
    #  berapa panjangnya? (1-10)


# For Loop Drawing Segitiga sama sisi siku bawah
# out=''
# for i in range(9): #data i adalah yang akan diinput panjang segitiga
#     for j in range(i+1):
#         out+=' * '
#     out+='\n'
# print(out)

# out1=''
# for a in reversed(range(5)): #inputan data panjang pada data i
#     for b in range(a):
#         out1+='*'
#     out1+='\n'
# print(out1)

# angka = 1
# while(angka<=10):
#     print(angka)
#     angka+=1

# listItem=list(range(1,11,2))
# print(listItem)
# for item in range (1,11,2):
#     print(item)
