import pandas as pd
def kriteria_IMT():
    kali =(berat) / ((tinggi/100) ** 2)
    print("\nDengan tinggi",tinggi,"dan berat",berat,"Anda memiliki BMI sebesar",kali)
    if kali >=30:
        print("\nAnda sudah masuk ke dalam kriteria Obesitas")
        print("Disarankan agar Anda melakukan diet")
    elif kali >=25:
        print("\nAnda masuk ke dalam kriteria Kelebihan berat")
        print("Disarankan agar Anda melakukan diet")
    elif kali >=18.5:
        print("\nAnda masuk ke dalam kriteria Normal")
        print("Jagalah berat badan Anda dengan olahraga,makan yang bergizi dan teratur, serta istirahat yang cukup")
    else :
        print("\nAnda masuk ke dalam kriteria kurus")
        print("Tingkatkan berat badan Anda dengan olahrga dan makan makanan yang bergizi")
def aktivitas(a):
    print("\nKebutuhan kalori dalam tubuh untuk aktivitas basal:",a)
    print("Seberapa sering Anda berolahraga\n")
    print("1. Sangat jarang olahraga")
    print("2. Jarang olahraga(1-3 hari per minggu)")
    print("3. Normal (3-5 hari per minggu)")
    print("4. Sering olahraga (6-7 hari per minggu)")
    print("5. Sangat sering olahraga (setiap hari bisa 2 kali sehari)")
    pilih = int(input("Masukkan pilihan 1-5: "))
    if pilih == 1:
        tingkat_aktivitas = a*1.2
    elif pilih == 2:
        tingkat_aktivitas = a*1.375
    elif pilih ==3:
        tingkat_aktivitas = a*1.55
    elif pilih == 4:
        tingkat_aktivitas = a*1.725
    elif pilih == 5:
        tingkat_aktivitas = a*1.9
    else:
        print("Input salah")  
    print("\nTotal kebutuhan kalori harian Anda : ", tingkat_aktivitas,"\n")
    target_berat = int(input("\nMasukkan berat yang Anda inginkan: "))
    kurangi_kalori = int(input("Pangkas Total kalori harian sebanyak: "))
    lama_diet = (berat-target_berat)/(kurangi_kalori/1000)
    kalori_diet = tingkat_aktivitas - kurangi_kalori
    print("Konsumsi Maksimal Kalori Selama diet: ", kalori_diet)
    print("Lama waktu diet yang Anda butuhkan:", lama_diet," minggu")
def dataframe():
    pokok11 = pd.DataFrame(Pokok1)
    pokok12 = pd.DataFrame(Pokok2)
    pokok13 = pd.DataFrame(Pokok3)
    print(a)
    print(pokok11,"\n")
    print(b)
    print(pokok12,"\n")
    print(c)
    print(pokok13,"\n")
    print("")
x = 1
while x!=0:
    print("1. Hitung Index Massa Tubuh")
    print("2. Daftar Menu Diet")
    print("3. Keluar")

    pilihan = int(input("Masukkan pilihan :"))
    if pilihan == 1:
        tinggi = int(input("Tinggi(cm): "))
        berat = int(input("berat(kg): "))
        usia = int(input("Usia:"))
        kriteria_IMT()
        pilih = input("\nIngin melakukan diet? y/t:")
        if pilih == 'y' or pilih == 'Y':
            gender = input("Jenis Kelamin (L/P):")
            if gender == 'L' or gender =='l' :
                BMR = 66+(13.7*berat)+(5*tinggi)-(6.8*usia)
                aktivitas(BMR)
            elif gender == 'p'or gender == 'P':
                BMR = 655+(9.6*berat)+(1.8*tinggi)-(4.7*usia)
                aktivitas(BMR)

    elif pilihan == 2:
        print("1. Makanan Pokok")
        print("2. Lauk Pauk")
        print("3. Sayuran")
        print("4. Buah")
        pilih = int(input("Lihat Menu : "))
        if pilih == 1:
            Pokok1 = {'Makanan':["Jagung Rebus",'Kentang Rebus','Ketan Putih','Kerupat','Lontong',
            'Nasi Putih','Nasi Putih Kentucky','Roti Tawar Serat Tinggi','Singkong Rebus','Talas Rebus','Ubi Rebus'],
            'Berat(gr)':[250,200,120,160,200,100,255,60,100,100,100],
            'Kalori':[90.2,166,217,32,38,175,349,149,146,98,125]}
            Pokok2 = {'Makanan':['Bubur','Crakers','Makaroni','Mie Instant','Nasi Tim','Nasi Uduk','Roti Tawar'],
            'Berat(gr)':[200,50,25,50,100,200,50], 
            'Kalori':[44,229,91,168,88,506,128]}
            Pokok3 = {'Makanan':['Bihun Goreng','Bubur Ayam','Bubur Sum-Sum','Kentang Goreng','Mie Goreng','Nasi Goreng','Soun Goreng',
            'Spaghetti','Tape singkong'], 'Berat(gr)':[150,200,100,150,200,100,100,300,150],
            'Kalori':[296,165,178,211,321,267,263,642,260]}
            a = "\t\tMakanan Golongan A\n"
            b = "\t\tMakanan Golongan B\n"
            c = "\t\tMakanan Golongan C\n"
            dataframe()
        elif pilih == 2:
            Pokok1 = {'Makanan':['Arsik','Ayam Panggang Bumbu Kuning','Ayam Panggang','Daging Panggang','Ikan Mas Pepes',
            'Sambal Goreng Tempe','Telur Asin Rebus','Telur Ayam Rebus'], 'Berat(gr)':[95,100,100,70,200,50,75,60],
            'Kalori':[94.05,129.4,164.3,150,143.5,116,138,97]}
            Pokok2 = {'Makanan':['Ati Ayam Goreng','Ayam Pop','Bakso Daging Sapi','Empal Daging','Ikan Bandeng Goreng','Ikan Baronang Goreng',
            'Ikan Bawal Goreng','Ikan Ekor Goreng','Ikan Kembung Goreng','Ikan Lele Goreng','Ikan Patin Goreng','Ikan Selar Goreng',
            'Ikan Tenggiri Goreng','IkanTeri Goreng','Ikan Tuna Goreng','Kerang Rebus','Macaroni Schootel','Tahu Bacem','Telur Mata Sapi'
            ,'Tempe Bacem','Tempe Goreng','Tenggiri Bumbu Kuning','Udang Goreng Besar'],'Berat(gr)':[50,200,100,100,160,120,120,100,80,60,200,
            40,60,50,60,100,50,100,60,50,50,90,80],'Kalori':[98,265,260,147,180.7,107.5,113.3,107.8,87.65,57.5,252.7,63.75,85.3,66,110,59,177,
            147,40,157,118,94.4,68.25]}
            Pokok3 = {'Makanan':['Abon Sapi','Ayam Goreng Kecap','Ayam Panggang','Chiken Wing / Sayap Ayam','Daging Balado','Dendeng Balado',
            'Gulai Ayam','Gulai Cumi','Gulai Kepala Ikan Kakap','Gulai Limpa','Gulai Tunjang','Ikan Kembung Balado','Ikan Teri','Kakap Goreng Tepung',
            'Kakap Panir','Keripik Tempe','Daging Cincang Bulat','Ayam Kentucky Paha Atas','Perkedel Jagung','Perkedel Kentang','Pu Yung Hai',
            'Rendang Daging','Sate Ayam','Ayam Kentucky Saya','Semur Ayam','Sambal Goreng Ati','Sambal Goreng Tempe Teri','Sambal Goreng Ati Sapi',
            'Sambal Goreng Udang + Kentang','Sop Sapi','Tahu Goreng','Tahu Isi','Tahu Sumedang','Telur dadar'], 'Berat(gr)':[50,75,80,50,50,40,100,100,
            320,60,80,125,50,80,75,25,50,150,50,50,50,75,100,150,50,100,150,100,100,260,100,150,100,75],'Kalori':[158,358.8,385.6,63.6,147,338,165.3,183,218.8,294,251,236.7,213,
            119,220,68,168,194.5,108,123,114,285.5,466,116,177.8,127,276,200,123,227,111,124,113,188]}
            a = "\t\tLauk Pauk Golongan A\n"
            b = "\t\tLauk Pauk Golongan B\n"
            c = "\t\tLauk Pauk Golongan C\n"
            dataframe()
        elif pilih ==3:
            Pokok1 = {'Makanan':['Apel','Apel Merah','Belimbing','Duku','Jambu Air','Jambu Biji','Jeruk Medan','Jeruk Pontianak','Jeruk Sunkist',
            'Mangga Manalagi','Nanas','Pepaya','Pir','Pisang Rebus','Salak','Semangka'],'Berat(gr)':[160,140,160,200,60,320,140,150,200,100,200,
            100,200,125,150,150],'Kalori':[92,82,80,81,35.4,157,46,67,40,72,104,46,80,136.5,63.6,48,]}
            Pokok2 = {'Makanan':['Alpukat','Anggur','Lengkeng','Melon','Mangga Harum Manis','Pir Hijau','Pisang Ambon','Pisang Barangan',
            'Pisang Mas','Pisang Raja','Sirsak'],'Berat(gr)':[100,125,100,120,300,200,100,200,125,150,125],'Kalori':[85,60,79,46,90,105,74.2,
            236,11,126,55]}
            Pokok3={'Makanan':['Durian Montong','Rambutan','sawo'],'Berat(gr)':[100,100,100],'Kalori':[134,69,92]}
            a = "\t\tSayuran Golongan A\n"
            b = "\t\tSayuran Golongan B\n"
            c = "\t\tSayuran Golongan C\n"
            dataframe()
        elif pilih == 4:
            Pokok1 = {'Makanan':['Acar Kuning','Bening Bayam','Cah Labu Siam','Sayur Asam','Sop Ayam Kombinasi','Sop Bayam',
            'Sop Kimlo','Sop Mutiara Jagung','Asop Oyong Misoa','Sop Telur Putuh'],'Berat(gr)':[75,50,100,100,100,50,100,100,100,
            100],'Kalori':[53,18,41.6,88,95,78,104,113,106,116]}
            Pokok2={'Makanan':['Sayur Lodeh','Cah Jagung Putren','Cah kacang Panjang','Sop Oyong Telur Puyuh','Setup Kentang Buncis',
            'Tumis Buncis','Tumis Daun Singkong','Tumis Kc. Panjang + Jagung'],'Berat(gr)':[100,100,100,100,100,100,120,125],'Kalori':[61,
            59,72,134,95,52,151,118]}
            Pokok3={'Makanan':['Buntil','Gudeg'],'Berat(gr)':[100,150],'Kalori':[106,132]}
            a = "\t\tBuah Golongan A\n"
            b = "\t\tBuah  Golongan B\n"
            c = "\t\tBuah  Golongan C\n"
            dataframe()
    elif pilihan == 3:
        x = 0
    else:
        print("Input Salah\n")