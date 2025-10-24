import os


def perkenlana():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selamat datang di restoran kami!")
    nama = input("Masukkan nama Anda: ")
    umur = input("Masukkan umur Anda: ")
    print(f"Halo, nama saya {nama} dan saya berumur {umur} tahun.")
perkenlana()
def daftar_menu():
    print("Menu Makanan:")
    print("1. Nasi Goreng")
    print("2. Mie Ayam")
    print("3. Sate Ayam")
    pilihan = input("Pilih menu (1-3): ")
    if pilihan == '1':
        print("Anda memilih Nasi Goreng.")
    elif pilihan == '2':
        print("Anda memilih Mie Ayam.")
    elif pilihan == '3':
        print("Anda memilih Sate Ayam.")
    else:
        print("Pilihan tidak valid.")
daftar_menu()
def daftar_harga ():
    harga_nasi_goreng = 15000
    harga_mie_ayam = 12000
    harga_sate_ayam = 20000
    print("Harga Makanan:")
    print(f"Nasi Goreng: Rp{harga_nasi_goreng}")
    print(f"Mie Ayam: Rp{harga_mie_ayam}")
    print(f"Sate Ayam: Rp{harga_sate_ayam}")
daftar_harga()
def hitung_total_harga():
    harga_nasi_goreng = 15000
    harga_mie_ayam = 12000
    harga_sate_ayam = 20000
    total_harga = 0
    while True:
        pilihan = input("Masukkan nomor menu yang ingin dipesan (1-3) atau 'q' untuk keluar: ")
        if pilihan == '1':
            total_harga += harga_nasi_goreng
            print("Nasi Goreng ditambahkan ke pesanan.")
        elif pilihan == '2':
            total_harga += harga_mie_ayam
            print("Mie Ayam ditambahkan ke pesanan.")
        elif pilihan == '3':
            total_harga += harga_sate_ayam
            print("Sate Ayam ditambahkan ke pesanan.")
        elif pilihan.lower() == 'q':
            break
        else:
            print("Pilihan tidak valid.")
    print(f"Total harga pesanan Anda adalah: Rp{total_harga}")
hitung_total_harga()
def ucapkan_selamat():
    print("Terima kasih telah memesan di restoran kami. Selamat menikmati makanan Anda!")
ucapkan_selamat()
def penutup():
    print("Sampai jumpa lagi!")
penutup()
def penutup():
    print("Sampai jumpa lagi!")
penutup()

