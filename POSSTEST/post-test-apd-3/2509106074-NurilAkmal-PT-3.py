NAMA_TERDAFTAR = "Nuril Akmal"    
NIM_TERDAFTAR  = 2509106074
biaya_langganan = 1500000 
print("=== Sistem Pembayaran Langganan Musik ===")
nama = input("Masukkan nama lengkap : ")
nim  = int(input("Masukkan NIM          : "))

if nama == NAMA_TERDAFTAR and nim == NIM_TERDAFTAR:
    print("Login berhasil. Selamat datang,", nama)
    print("Biaya langganan:", biaya_langganan)
 
    print("=== Pilihan Paket ===")
    print("1. Bronze  (Admin 1%)")
    print("2. Silver  (Admin 3%)")
    print("3. Gold    (Admin 5%)")
    print("4. Platinum(Admin 7%)")

    pilihan = input("Pilih paket (1/2/3/4): ")

    if pilihan == "1":
        admin = biaya_langganan * 0.01
        total = biaya_langganan + admin
        print("=== Paket Bronze ===")
        print("Keuntungan: Akses dasar ke lagu-lagu populer")
        print("Total bayar:", total)

    elif pilihan == "2":
        admin = biaya_langganan * 0.03
        total = biaya_langganan + admin
        print("=== Paket Silver ===")
        print("Keuntungan: Akses lagu premium, playlist kustom")
        print("Total bayar:", total)

    elif pilihan == "3":
        admin = biaya_langganan * 0.05
        total = biaya_langganan + admin
        print("=== Paket Gold ===")
        print("Keuntungan: Premium + playlist kustom + mode offline")
        print("Total bayar:", total)

    elif pilihan == "4":
        admin = biaya_langganan * 0.07
        total = biaya_langganan + admin
        print("=== Paket Platinum ===")
        print("Keuntungan: Semua fitur + playlist kustom + mode offline + konten eksklusif artis")
        print("Total bayar:", total)

    else:
        print("Pilihan paket tidak tersedia.")

else:
    print("Login gagal! Nama atau NIM salah.")
