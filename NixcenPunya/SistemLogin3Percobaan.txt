pw_benar = "CikalCibolangKaler"
percobaan = 0

while percobaan < 3:
    pw_input = input("Masukkan password: ")
    if pw_input == pw_benar: 
        print("Login berhasil!")
        break
    
    else:
        percobaan += 1
        print("Password salah. Percobaan ke-", {percobaan})
    if percobaan == 3:
        print("Akun terkunci")
