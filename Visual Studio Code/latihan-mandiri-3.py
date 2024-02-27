masukan = input("Masukkan bulan (1-12): ")

try:
    bulan = int(masukan)
    if bulan == 2:
        print("29 hari, karena tahun kabisat")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print("30 hari")
    elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print("31 hari")
    else:
        print("Bulan tidak valid")
except:
    print("Bulan tidak boleh huruf atau simbol!")