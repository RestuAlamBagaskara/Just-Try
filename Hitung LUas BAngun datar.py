def Lpersegi(s):
    luas = s*s
    return luas
def Lpersegip(a,b):
    luas = a*b
    return luas
def Lsegitiga(a,t):
    luas = 0.5*a*t
    return luas
def Llingkaran(r):
    luas = 3.14*r**2
    return luas
def Ljajargenjang(a,t):
    luas = a*t
    return luas
def Kpersegi(s):
    kel =  4*s
    return kel
def Kpersegip(a,b):
    kel =  2*(a+b)
    return kel
def Ksegitiga(a,b,c):
    kel=a+b+c 
    return kel
def Klingkaran(r):
    kel= 2*r*3.14
    return kel
def Kjajargenjang(a,t):
    kel = 2*(a+t)
    return kel
def menu():
    print('1. Persegi')
    print('2. Persegi Panjang')
    print('3. Segitiga')
    print('4. Lingkaran')
    print("5. Jajar Genjang")
    print('6. Keluar')
    
while True:
    print('1. Hitung luas')
    print ('2. Hitung Keliling')
    print('3. keluar')

    pil = input("1/2/3 :")
    if pil =='1':
        menu()

        pil = input("1/2/3/4/5/6 :")
        if pil =='1':
            s = int(input("Sisi : "))
            print(Lpersegi(s))
        elif pil =='2':
            a = int(input("Panjang :"))
            b = int(input("Lebar :"))
            print(Lpersegip(a,b))
        elif pil=='3':
            a = int(input('Alas :'))
            t = int(input('tinggi :'))
            print(Lsegitiga(a,t))
        elif pil=='4':
            r = int(input(" jari-jari :"))
            print(Llingkaran(r))
        elif pil=='5':
            a = int(input("Alas :"))
            t = int(input("Tinggi :"))
            print(Ljajargenjang(a,t))
        else:
            print(" Oke Keluar")
            break
    elif pil =='2':
        menu()
        
        pil = input("1/2/3/4/5/6 :")
        if pil =='1':
            s = int(input("Sisi : "))
            print(Kpersegi(s))
        elif pil =='2':
            a = int(input("Panjang :"))
            b = int(input("Lebar :"))
            print(Kpersegip(a,b))
        elif pil=='3':
            a = int(input('sisi A :'))
            b = int(input('sisi B :'))
            c= int(input(" sisi C : "))
            print(Ksegitiga(a,b,c))
        elif pil=='4':
            r = int(input(" jari-jari :"))
            print(Klingkaran(r))
        elif pil =='5':
            a = int(input("Alas :"))
            t = int(input(" Sisi Miring :"))
            print(Kjajargenjang(a,t))
        else:
            print(" Oke Keluar")
            break
    else:
        print("Oke Keluar")
        break