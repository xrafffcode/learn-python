print("-selamat datang di ATM -Bersama untuk dunia akhirat-")
customer= input("Masukan nama customer:")
print("Nama customer:", customer)

total1 = 0
jenis1 = ""
tabung = 0

def fungsitabung():
    global total1
    global jenis1
    global tabung
    print("---Tabungan Masa Depan---")
    print("1. Tabungan Haji       -Rp. 100000")
    print("2. Tabungan Pensiun    -Rp. 200000 ")
    print("3. Tabungan Pendidikan -Rp. 75000")
    nomor= int(input("Masukan jenis tabungan:"))
    tabung= int(input("Berapa bulan menabung:"))

    if nomor == 1:
        total1 = tabung * 100000
        print(tabung,"Tabungan Haji:",total1)
        jenis1 = ("Haji")
    elif nomor == 2:
        total1 = tabung * 200000
        print(tabung,"Tabungan Pensiun:", total1)
        jenis1 = ("Pensiun")
    elif nomor == 3:
        total1 = tabung * 75000
        print (tabung,"Tabungan Pendidikan:",total1)
        jenis1 = ("Pendidikan")
        fungsitabung()

def ulangi ():
    x = 0
    while x == 0:
        pilih = input("Menabung Lagi (y/t) :")
        if pilih == "y" or pilih == "Y" :
            programkasir()
        elif pilih == "t" or pilih == "T" :
            print("Terimakasih sudah menabung di Bank Rafa")
            break
        else:
            print("Selamat Menabung")

def programkasir():
    fungsitabung()

    totalsemua = total1
    print("\nTotal semua yang harus ditabung", totalsemua)
    uang = int(input("Uang Tabungan Pembeli: Rp."))
    bunga = int(uang - totalsemua)
    print("uang bunga",bunga)
    print("\n----------------------------------------------")
    print("----------------STRUK PEMBELIAN---------------")
    print("----------------------------------------------")
    print("Nama          :", customer)
    print("Tabung        :", tabung, jenis1, "-", total1)
    print("Tagihan       :Rp.", totalsemua)
    print("Uang          :Rp.", uang)
    print("Bunga         :Rp.", bunga)
    print("----------------------------------------------")
    print("----------------------------------------------")
programkasir()