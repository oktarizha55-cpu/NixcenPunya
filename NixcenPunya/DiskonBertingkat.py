Diskon = int(input("Masukkan total belanja: "))
if Diskon >= 500000:
    print("Mendapatkan diskon 20%")
elif Diskon >= 300000:
    print("Mendapatkan diskon 10%")
elif Diskon >= 100000:
    print("Mendapatkan diskon 5%")
elif Diskon < 100000:
    print("Tidak ada diskon")
