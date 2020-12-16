saldo=[]
berat=[]
x = 0
while x!=1:
    print("Login Sebagai:")
    print("1. Admin")
    print("2. Nasabah")
    print("3. Keluar")
    pilih = int(input("Masukkan pilihan: "))
    if pilih == 1:
        #usernama and passwd = admin1
        username = input("Username:")
        passwd = input("Password: ")
        if username == 'admin1' and passwd == 'admin1':
            print("1. Total Tabungan admin ")
            print("2. Total Berat sampah yang terkumpul")
            pilih = int(input("Pilih: "))
            if pilih == 1:
                total = sum(saldo)
                print("Tabungan Admin saat ini : ", total)
            elif pilih == 2:
                bt = sum(berat)
                print("Berat sampah yang terkumpul: ", bt, "Kg")
        else:
            print("Username atau password anda salah")
    elif pilih == 2:
        print("1. Harga Sampah")
        print("2. Setor Sampah")
        pilih = int(input(" Pilih : "))
        if pilih == 1:
            print("")
            print("|\tJenis\t|\tHarga/kg\t|")
            print("|=======================================|")
            print("|\tSampah Plastik\t|\tRp.2500\t|")
            print("|\tSampah Kertas\t|\tRp.1000\t|")
            print("|\tSampah Kaleng\t|\tRp.3000\t|")
        elif pilih == 2:
            print("|\tPilih jenis sampah:\t|")
            print("|1. \tSampah Plastik\t|")
            print("|2. \tSampah Kertas\t|")
            print("|3. \tSampah Kaleng\t|")
            pilihsampah = int(input("Pilih Jenis Sampah: "))
            berat_1 = int(input("Masukkan Berat Sampah Anda (kg):"))
            berat.append(berat_1)
            if pilihsampah == 1:
                saldo_1 = berat_1*2500
                saldo.append(saldo_1)
                print("Uang Anda Terima sebesar: Rp.",saldo_1)
            elif pilihsampah == 2:
                saldo_1 = berat_1*1000
                saldo.append(saldo_1)
                print("Uang Anda Terima sebesar: Rp.",saldo_1)
            elif pilihsampah == 3:
                saldo_1 = berat_1*3000
                saldo.append(saldo_1)
                print("Uang Anda Terima sebesar: Rp.",saldo_1)
    elif pilih == 3:
        print("\n========-Terima Kasih Telah Menjaga Lingkungan-========")
        print("\nYakin Ingin Keluar y/t ")
        pilih = input("")
        if pilih=='y' or pilih =='Y':
            x = 1
        elif pilih =='t' or pilih =='T':
            print("")
        else:
            print("Input salah")
    else:
        print("Menu Tidak Tersedia")