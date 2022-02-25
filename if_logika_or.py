print("Membuat Predikat Nilai")

pre = "Predikat anda"
nilai = input("Masukkan Predikat Nilai Anda : ")

if (nilai=="A") or (nilai=="a") :
    print(pre, nilai,",Nilai anda sangat baik")

elif (nilai=="B") or (nilai=="b") :
    print(pre, nilai,",Nilai anda baik")

elif (nilai=="C") or (nilai=="c") :
    print(pre, nilai,",Nilai anda cukup")

elif (nilai=="D") or (nilai=="d") :
    print(pre, nilai,",Nilai anda kurang")

elif (nilai=="E") or (nilai=="e") :
    print(pre, nilai,",Nilai anda sangat kurang")

else :
    print("Kode tidak terdefinisi")