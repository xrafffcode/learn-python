# Belajar Membuat Program For Loop

banyak = int(input("Berapa Banyak Data? "))

nama = []
umur = []

for i  in range(0, banyak):
    print(f"Data Ke {i}")
    input_nama = input("Nama : ")
    input_umur = int(input("Umur : "))

    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun")
    
