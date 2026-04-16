total_belanja = int(input("Masukkan total belanja: "))
if total_belanja >= 100000:
    print("Mendapatkan diskon 10%")
    diskon = total_belanja *0.1
else:
    print("Tidak mendapatkan diskon")
    diskon = 0
total_bayar = total_belanja - diskon
print(f"Total belanja chikal: Rp.{total_belanja:,},Diskon yang di dapat: Rp. {diskon:,}, Total yang harus di bayar: Rp. {total_bayar:,}")
