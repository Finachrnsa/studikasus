def hitung_usia():
    tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    tahun_ini = 2024
    usia = tahun_ini - tahun_lahir
    print("Usia Anda saat ini adalah:", usia, "tahun")

def hitung_angsuran():
    tahun_angsuran = int(input("Masukkan tahun angsuran: "))
    tahun_ini = 2024
    sisa_tahun = tahun_angsuran - tahun_ini
    print("Sisa tahun angsuran adalah:", sisa_tahun, "tahun")

def hitung_bmi():
    berat = float(input("Masukkan berat badan Anda (kg): "))
    tinggi = float(input("Masukkan tinggi badan Anda (m): "))
    bmi = berat / (tinggi ** 2)
    print("BMI Anda adalah:", bmi)

def main():
    while True:
        print("\nMenu:")
        print("A. Hitung usia saat ini")
        print("B. Hitung sisa tahun angsuran")
        print("C. Hitung berat badan BMI")
        print("D. Keluar")

        pilihan = input("Pilih menu (A/B/C/D): ").upper()

        if pilihan == 'A':
            hitung_usia()
        elif pilihan == 'B':
            hitung_angsuran()
        elif pilihan == 'C':
            hitung_bmi()
        elif pilihan == 'D':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "_main_":
    main() 