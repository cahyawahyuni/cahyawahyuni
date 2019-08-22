# Tugas 1 count words
def countWords(a):
    b=a.split(' ')
    print(len(b))

countWords('Budi pergi ke pasar')
countWords('Ayah membeli singkong dan sayur bayam')

# Tugas 2 small enough
def smallEnough(a,b):
    c=0
    check=False
    for i in a:
        c+=i
        if c < b:
            check=True
        if c > b:
            check=False
    print(check)

smallEnough([100,78],200)
smallEnough([100,15,80],150)

# Tugas 3 removeDuplicate
def removeDuplicate(a):
    b = a.split(' ')
    newSet = set()
    for i in b:
        newSet.add(i)
    newList=sorted(list(newSet))
    c=0
    out=''
    for j in newList:
        if c<(len(newList)-1):
            out+=j
            out+=' '
        else:
            out+=j
        c+=1
    print("'"+out+"'")

removeDuplicate('alpha beta beta gamma gamma')
removeDuplicate('ayam ayam bebek ikan ayam sapi zebra kerbau kerbau')

# Tugas 4 stringy
def stringy(a):
    out=''
    for i in range(a):
        if i % 2 == 0:
            out+='1'
        elif i % 2 != 0:
            out+='0'
    print(out)

stringy(12)
stringy(4)
stringy(5)

# Tugas 5 Wave
def wave(a):
    a = a.lower()
    out=[]
    for i in range(len(a)):
        b=''
        c=0
        for j in a:
            if c==i:
                b+=j.upper()
            else:
                b+=j
            c+=1
        out.append(b)
    print(out)

wave('Hello')
wave('pepaya')
        







