def SelectionSort(val):
    for isi in range(len(val) - 1, 0, -1):
        max = 0
        for lokasi in range(1, isi + 1):
            if val[lokasi] > val[max]:
                max = lokasi
        temp = val[isi]
        val[isi] = val[max]
        val[max] = temp


DaftarAngka = [22, 8, 82, 69, 3, 55, 15, 26]
SelectionSort(DaftarAngka)
print(DaftarAngka)