try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    result = "Positif" if bilangan > 0 else ("Negatif" if bilangan < 0 else "Nol")
    print(result)
except:
    print("Input harus berupa bilangan bulat")