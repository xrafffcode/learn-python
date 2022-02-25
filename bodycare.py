import time
waktu = time.asctime(time.localtime(time.time()))

print("Penjualan Body Care")
nomer = input("Masukan Nomer Pembeli : ")
print("Nomer Pembeli : ", nomer)

total1 = 0
nominal1 = ""
jumlah = 0

def fungsiproduk1():
    global total1
    global jenis1
    print("Daftar Body Care")
    print("1. Body Lotion Scarlett Whitening Romansa - RP 50000")
    print("2. Body Lotion Scarlett Whitening Charming - RP 50000")
    print("3. Body Lotion Scarlett Whitening Freshy - RP 50000 ")
    print("4. Body Lotion Scarlett Whitening Fantasia - RP 50000")
    print("5. Brightening Shower Scrub Pomegrante - RP 75000")
    print("6. Brightening Shower Scrub Cucumber - RP 75000")
    print("7. Brightening Shower Scrub Mango - RP 75000")
    print("8. Body Scrub Scarlett Whitening - RP 65000")
    pilih = int(input("Masukan Pilihan :"))
    jumlah = int(input("Jumlah produk : "))

    if pilih == 1:
        total1 = jumlah * 50000
        print(jumlah, "produk Body Lotion Scarlett Whitening Romansa = Rp", total1)
        jenis1 = ("Body Lotion Scarlett Whitening Romansa")

    elif pilih == 2:
        total1 = jumlah * 50000
        print(jumlah, "produk Body Lotion Scarlett Whitening Charming = Rp", total1)
        jenis1 = ("Body Lotion Scarlett Whitening Charming")

    elif pilih == 3:
        total1 = jumlah * 50000
        print(jumlah , "produk Body Lotion Scarlett Whitening Freshy = Rp", total1)
        jenis1 = ("Body Lotion Scarlett Whitening Freshy")

    elif pilih == 4:
        total1 = jumlah * 50000
        print(jumlah, "produk Body Lotion Scarlett Whitening Fantasia = Rp", total1)
        jenis1 = ("Body Lotion Scarlett Whitening Fantasia")

    elif pilih == 5:
        total1 = jumlah * 75000
        print(jumlah, "produk Brightening Shower Scrub Pomegrante = Rp", total1)
        jenis1 = ("Brightening Shower Scrub Pomegrante")

    elif pilih == 6:
        total1 = jumlah * 75000
        print(jumlah, "produk Brightening Shower Scrub Cucumber = Rp", total1)
        jenis1 = ("Brightening Shower Scrub Cucumber")
        
    elif pilih == 7:
        total1 = jumlah * 75000
        print(jumlah, "produk Brightening Shower Scrub Mango = Rp", total1)
        jenis1 = ("Brightening Shower Scrub Mango")

    elif pilih == 8 :
        total1 = jumlah * 65000
        print(jumlah, "produk Body Scrub Scarlett Whitening = Rp", total1)
        jenis1 = ("Body Scrub Scarlett Whitening")

    else :
        print("Pilihan tidak ada dalam menu, silahkan pilih menu yang ada pada daftar")
        fungsiproduk1()

def fungsiproduk2():
    global total2
    global jenis2
    print("\n ──── Menu Paket Body Care ────")
    print("1. Body Scrub , Shower Scrub - Rp 130000")
    print ("2. Body Lotion , Shower Scrub - Rp 115000")
    print ("3. Body Scrub , Body Lotion - Rp 100000")
    nomor = int(input("Masukan Pilihan :"))
    paket = int(input("Jumlah Paket:"))

    if nomor == 1:
        total2 = paket * 130000
        print(paket, "Body Scrub, Shower Scrub = Rp",total2)
        jenis2 = ("Body Scrub, Shower Scrub")

    elif nomor == 2:
        total2 = paket * 115000
        print(paket, "Body Lotion, Shower Scrub = Rp", total2)
        jenis2 = ("Body Lotion, Shower Scrub")

    elif nomor ==3:
        total2 = paket * 100000
        print(paket, "Body Scrub, Body Lotion = Rp", total2)
        jenis2 = ("Body Scrub, Body Lotion")

    else :
        print ("Pilihan tidak ada dalam menu, silahkan pilih kembali")
        fungsiproduk2()


    
def ulang():
    x = 0
    while x == 0:
        pilih = input("Transaksi Lagi (y/t) : ")
        if pilih == "y" or pilih == "Y":
            programkasir()
        elif pilih == "t" or pilih == "T":
            print("Terima Kasih")
            break
        else:
            print("Silahkan Order")

def programkasir():
    fungsiproduk1()
    totalsemua = 0
    totalsemua = total1
    print("\nTotal Harus Dibayar: Rp", totalsemua)
    uang = int(input("Uang Tunai Pembeli: Rp."))
    kembalian = int(uang - totalsemua)
    print("Kembalian :" , kembalian)

    print("\n=======================================")
    print("==========S T R U K   B E L I==========")
    print("=======================================")
    print("")
    print(waktu)
    print("")
    print("Kasir : Muhamad Rafli")
    print("")
    print("Nama         :", nomer)
    print("Beli         :", jumlah, nominal1, "-", total1)
    print("Tagihan      :", totalsemua)
    print("Uang         :", uang)
    print("Kembalian    :", kembalian)
    print("=======================================")
    print("=======================================")
    ulang()

programkasir()