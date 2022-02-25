import time
waktu = time.asctime(time.localtime(time.time()))

print("Penjualan Pulsa")
nomer = input("Masukan Nomer Pembeli : ")
print("Nomer Pembeli : ", nomer)

total1 = 0
nominal1 = ""
jumlah = 0

def fungsinominal():
    global total1
    global nominal1
    print("\n----Pilih Nominal Pulsa----")
    print("1. 5000 Rupiah")
    print("2. 10,000 Rupiah")
    print("3. 20,000 Rupiah")
    print("4. 50,000 Rupiah")
    print("5. 100,000 Rupiah")
    pilih = int(input("Masukan Pilihan: "))
    jumlah = 1

    if pilih == 1:
        total1 = jumlah * 7000
        print("5000 Pulsa = Rp", total1)
        nominal1 = ("5000 Rupiah")

    elif pilih == 2:
        total1 = jumlah * 12000
        print("10,000 Pulsa = Rp", total1)
        nominal1 = ("10,000 Rupiah")

    elif pilih == 3:
        total1 = jumlah * 22000
        print("20,000 Pulsa = Rp", total1)
        nominal1 = ("20,000 Rupiah")

    elif pilih == 4:
        total1 = jumlah * 52000
        print("50,000 Pulsa = Rp", total1)
        nominal1 = ("50,000 Rupiah")

    elif pilih == 5:
        total1 = jumlah * 102000
        print("100,000 Pulsa = Rp", total1)
        nominal1 = ("100,000 Rupiah")

    else:
        print("Pilihan Tidak Ada Silahkan Masukan Lagi")
        fungsinominal()
    
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
    fungsinominal()
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