nilai = int(input("Menghitung Nilai: "))
absensi = int(input("Menghitung Absensi: "))
if nilai > 70 and absensi > 50:
    print ("lulus")
elif (nilai < 70 and absensi > 70) or (nilai > 70 and absensi < 50):
    print("Tidak lulus tapi bisa Perbaikan Nilai")
else:
    print("Tidak lulus dan Tidak bisa Perbaikan Nilai")    
