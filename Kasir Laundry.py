import pandas as pd
def struk(n,j,k):
    print("")
    print("=========STRUK BINATU=========")
    print("Berat/Jumlah barang  :",k)
    print("Biaya/(kg/satuan)    :",n)
    print("Total                :", j)
    print("=========Terima Kasih=========")
    print("=====Telah Memercayai Kami=====")
    print("")
def waktu_jasa():
    print("1. Reguler(2-3 hari)")
    print("2. Kilat(1 hari)")
    print("3. Express(8 jam)")
    pilih = int(input("Pilih kecepatan : "))
    berat = int(input("Berat pakaian(kg) : "))
    if pilih == 1:
        jumlah_bayar = a*berat
        struk(a, jumlah_bayar, berat)
    elif pilih == 2:
        jumlah_bayar = b*berat
        struk(b, jumlah_bayar, berat)
    elif pilih == 3:
        jumlah_bayar = c*berat
        struk(c, jumlah_bayar, berat)
def bayar_satuan(n):
    berat = int(input("Jumlah Cucian:"))
    jumlah_bayar = berat*n
    print(jumlah_bayar)
    struk(n,jumlah_bayar,berat)
    
x = 1
while x!=0:
    print("\t\tMenu Kasir Binatu\n")
    print("1. Kiloan")
    print("2. Satuan")
    print("3. Keluar")
    pilihan = int(input("Masukkan Pilihan 1/2 :"))
    if pilihan == 1:
        Menu = {'Jenis':['','Cuci Komplet Reguler','Cuci Komplet Kilat','Cuci Komplet Express','Cuci Kering Reguler','Cuci Kering Kilat',
        'Cuci Kering Express','Setrika Reguler','Setrika Kliat','Setrika Express'],'Lama Pengerjaan':['','2-3 hari','1 hari','8 jam','2-3 hari',
        '1 hari','8 jam','2-3 hari','1 hari','8 jam'], 'Biaya(Rp.)':['',7000,12000,15000,6000,9000,10000,6000,9000,10000]}
        Menu_kiloan = pd.DataFrame(Menu)
        print ("\t\tDaftar Harga Kiloan\n")
        print(Menu_kiloan)
        print("")
        print("1. Cuci Komplet")
        print("2. Cuci Kering")
        print("3. Setrika")
        pilihan = int(input("Pilih Jasa: "))
        if pilihan ==1:
            a = 7000
            b= 12000
            c=15000
            waktu_jasa()
        elif pilihan == 2:
            a = 6000
            b= 9000
            c=10000
            waktu_jasa()
        elif pilihan == 3:
            a = 6000
            b= 9000
            c=10000
            waktu_jasa()
        else:
            print("Jasa tidak tersedia")
    elif pilihan ==2:
        Menu = {'Barang':['','Bantal/guling mini','Bantal/guling sedang','Bantal/guling besar','Boneka mini','Boneka sedang','Boneka besar','Boneka besar sekali',
        'blouse/celana panjang','skirt & blouse','celana pendek biasa/ jeans','celana panjang jeans','kemeja lengan panjang','kmeja lengan pendek',
        'jaket non kulit'], 'biaya':['',7000,10000,12000,5000,8000,10000,23000,5000,5000,5000,7000,8000,5000,10000]}
        menu = pd.DataFrame(Menu)
        print("\t\tDaftar Harga Satuan\n")
        print(menu)
        print("")
        pilih = int(input("Pilih Barang: "))
        if pilih == 1 or pilih == 11:
            n = 7000
            bayar_satuan(n)
        elif pilih == 2 or pilih == 6 or pilih == 14:
            n = 10000
            bayar_satuan(n)
        elif pilih ==3 :
            n = 12000
            bayar_satuan(n)
        elif pilih ==4 or pilih ==8 or pilih ==9 or pilih ==10 or pilih == 13:
            n = 5000
            bayar_satuan(n)
        elif pilih ==5 or pilih ==12:
            n = 8000
            bayar_satuan(n)
        elif pilih ==7:
            n = 23000
            bayar_satuan(n)
        else:
            print("Jasa Tidak Tersedia")
    elif pilihan == 3:
        x = 0
    else:
        print("Pilihan tidak tersedia")