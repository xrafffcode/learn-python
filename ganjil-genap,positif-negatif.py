input_bilangan = input("Masukan Bilangan : ")

bil = int(input_bilangan)

if (bil < 0) and (bil % 2 ==0):
    print (bil, "Merupakan genap negatif")

elif (bil < 0) and (bil % 2 ==1):
    print (bil, "Merupakan ganjil negatif")

elif (bil > 0) and (bil % 2 ==0):
    print (bil, "Merupakan genap positif")

elif (bil > 0) and (bil % 2 ==1):
    print (bil, "Merupakan ganjil positif")

else :
    print (bil, "Merupakan bilangan istimewa")