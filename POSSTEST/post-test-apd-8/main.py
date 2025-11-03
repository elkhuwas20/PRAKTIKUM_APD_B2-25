# main.py
import sys
from utils import bersihkan_layar, hitung_peserta
from data import admin, users
from fungsi_event import tampilkan_semua_event
from fungsi_user import menu_user
from fungsi_admin import menu_admin

while True:
    bersihkan_layar()
    print("=" * 60)
    print("SISTEM MANAJEMEN EVENT WEB3 & HACKATHON".center(60))
    print("=" * 60)
    print("1. Login")
    print("2. Register")
    print("3. Lihat Event (Guest)")
    print("4. Keluar")
    print("=" * 60)
    
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == '1':
        user = input("Username: ")
        pwd = input("Password: ")
        if user in admin and admin[user] == pwd:
            menu_admin(user)
        elif user in users and users[user] == pwd:
            menu_user(user)
        else:
            print("Username atau password salah!")
            input("\nTekan Enter...")

    elif pilihan == '2':
        nama = input("Username baru: ")
        pwd = input("Password: ")
        users[nama] = pwd
        print("Registrasi berhasil!")
        input("\nTekan Enter...")

    elif pilihan == '3':
        tampilkan_semua_event()
        print(f"\nTotal peserta di semua event: {hitung_peserta()}")
        input("\nTekan Enter...")

    elif pilihan == '4':
        print("Terima kasih! Sampai jumpa!")
        sys.exit()

    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter...")
