# Contoh 3.3

a = input("Masukkan bilangan pertama: ")
b = input("Masukkan bilangan kedua: ")
c = input("Masukkan bilangan ketiga: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a > b and a > 3:
        print(a, "adalah bilangan terbesar")
    elif b > a and b > c:
        print(b, "adalah bilangan terbesar")
    elif c > a and c > b:
        print(c, "adalah bilangan terbesar")
except:
    print("Inputan tidak valid, isi menggunakan angka!")