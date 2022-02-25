def BubbleSort(val):
    for passnum in range(len(val) - 1, 0, -1):
        for i in range(passnum):
            if val[i] > val[i + 1]:
                temp = val[i]
                val[i] = val[i + 1]
                val[i + 1] = temp
DaftarAngka = [26, 4, 2, 99, 5, 17, 111, 0]
BubbleSort(DaftarAngka)
print(DaftarAngka)