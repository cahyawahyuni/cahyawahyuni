#Function : isinya block of code yang bisa dipakai lagi berulang2
# def SegitigaMaker():
#     a=0
#     output=''
#     x=4
#     ganjil=1
#     while(a<x):
#         b=0
#         while(b<(x-1)-a):
#             output+=' '
#             b+=1
#         c=0
#         while(c<ganjil):
#             output+= '*'
#             c+=1
#         ganjil+=2
#         output+='\n'
#         a+=1 
#     print(output)
# SegitigaMaker()
# SegitigaMaker()
# SegitigaMaker()
# SegitigaMaker()

#Function with parameter
# def namaku(nama) : #parameter nama akan ke print sesuai dengan isian saat function dipanggil
#     print(nama + ' Susilo')
# namaku('Adi')
# namaku('Budi')
# namaku('Caca')

# def hitungparkir(masuk,keluar):
#     totaljam=abs(keluar-masuk)
#     totalbiaya=totaljam*3000
#     print(totalbiaya)
# hitungparkir(7,10)
# hitungparkir(24,7)

# def removechart(word,remove):
#     x=word.replace(remove,'')
#     print(x)
#     #bisa juga print(word.replcae(remove,''))
# removechart('apa','a')
# removechart('alami','i')

def suit(player1,player2):
    if(player1==player2):
        print('Seri')
    elif(player1=='kertas'):
        if(player2=='gunting'):
            print('player 1 memilih {} dan player 2 memilih {}, player2 menang'.format(player1,player2))
        elif(player2=='batu'):
            print('player 1 memilih {} dan player 2 memilih {}, player1 menang'.format(player1,player2))    
    elif(player1=='batu'):
        if(player2=='kertas'):
            print('player 1 memilih {} dan player 2 memilih {}, player2 menang'.format(player1,player2))
        elif(player2=='gunting'):
            print('player 1 memilih {} dan player 2 memilih {}, player1 menang'.format(player1,player2))
    elif(player1=='gunting'):
        if(player2=='batu'):
            print('player 1 memilih {} dan player 2 memilih {}, player2 menang'.format(player1,player2))
        elif(player2=='kertas'):
            print('player 1 memilih {} dan player 2 memilih {}, player1 menang'.format(player1,player2))        
    # if(player1=='kertas' and player2=='batu'):
    #     print('Player1 Win')
    # if(player1=='kertas' and player2=='gunting'):
    #     print('Player2 Win')
    # if(player1=='batu' and player2=='kertas'):
    #     print('Player2 Win')
    # if(player1=='batu' and player2=='gunting'):
    #     print('Player1 Win')
    # if(player1=='gunting' and player2=='batu'):
    #     print('Player2 Win')
    # if(player1=='gunting' and player2=='kertas'):
    #     print('Player1 Win')

suit('batu','batu')
suit('kertas','batu')
suit('batu','gunting')
suit('gunting','batu')


