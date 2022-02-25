def InsertionSort(val):
    for index in range(1, len(val)):
        valueaktif = val[index]
        posisi = index
        while posisi > 0 and val[posisi - 1] > valueaktif:
            val[posisi] = val[posisi - 1]
            posisi = posisi - 1
        val[posisi] = valueaktif

DaftarAngka = [23, 6, 1, 89, 5, 7, 11, 221]
InsertionSort(DaftarAngka)
print(DaftarAngka)