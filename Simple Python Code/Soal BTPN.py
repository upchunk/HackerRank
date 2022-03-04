"""
Sistem penghitung uang kembalian

Constraint Input pertama:
Mesin hanya menerima total harga yang perlu kamu bayar dengan angka kelipatan 1.000.

Constraint Input kedua:
Karena Uang pecahan yang kamu bawa hanya uang 100.000an. Input angka hanya boleh  kelipatan 100.000

Constraint tambahan, input kedua harus lebih besar dari input pertama

Output:
Print uang kembalian yang perlu dikeluarkan dari sistem dengan jumlah pecahan tersedikit

Uang kembalian yang tersedia:
100.000
50.000
20.000
5.000
1.000

Contoh:

67000 100000 -> 20000, 5000, 5000, 1000, 1000, 1000
150000 100000 -> Tidak valid
4500 100000 -> Tidak valid
45000 150000 -> Tidak valid
90000 100000 -> 5000, 5000
5000 200000 -> 100000, 50000, 20000, 20000, 5000
"""

input1 = input("Masukkan Jumlah Yang Harus dibayar: ")
input2 = input("Masukkan Jumlah Pembayaran: ")

harga = int(input1)

bayar = int(input2)
if harga % 1000 != 0:
    print ("Tidak Valid")

elif bayar % 100000 != 0:
    print ("Tidak Valid")
    
elif bayar < harga:
    print ("Tidak Valid")

else:
    if bayar > 100000:
        ribu100 = harga % 100000
        lembar100 = harga / 100000
        ribu50 = ribu100 % 50000
        lembar50 = 
    ribu20 = harga % 20000
    ribu5 = harga % 5000
    ribu1 = harga % 1000
    
    