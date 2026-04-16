kwh = int(input("Menghitung Jumlah Kwh Yang Digunakan: "))
if kwh <= 100:
    total = kwh * 500
elif kwh <= 300:
    total = kwh * 1000
elif kwh <= 1000:
    total = kwh * 2000
print ("Total tagihan listrik: {total} rupiah")
