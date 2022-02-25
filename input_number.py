# Belajar Input Number


print("Masukan bilangan pertama:")
b1 = int( input() )

print("Masukan bilangan Kedua:")
b2 = int( input() )

print("Masukan bilangan Ketiga:")
b3 = int( input() )

if (b1 > b2) and (b1 > b3):
    print("Bilangan Pertama adalah Bilangan Terbesar")

elif (b2 > b1) and (b2 > b3):
    print("Bilangan Kedua adalah Bilangan Terbesar")

else:
    print("Bilangan Ketiga adalah Bilangan Terbesar")