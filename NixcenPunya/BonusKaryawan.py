masa_kerja = int(input("Masukkan masa kerja karyawan (dalam tahun): "))
performa = input("Masukkan performa karyawan (baik/buruk): ")

if masa_kerja >= 5 and performa == "baik":
    print("Mendapatkan bonus besar")
elif masa_kerja >= 5 and performa == "buruk":
    print("Mendapatkan bonus kecil")
else:
    print("Tidak mendapatkan bonus")
