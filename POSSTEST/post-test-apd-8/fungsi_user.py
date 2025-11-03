# fungsi_user.py
from utils import bersihkan_layar, cek_angka, cari_event
from fungsi_event import tampilkan_semua_event
from data import events

def menu_user(nama_user):
    while True:
        bersihkan_layar()
        print(f"\nSelamat datang, {nama_user}!")
        print("=" * 50)
        print("1. Lihat Event")
        print("2. Daftar Event")
        print("3. Logout")
        print("=" * 50)

        pilih = input("Pilih menu (1-3): ")

        if pilih == '1':
            bersihkan_layar()
            tampilkan_semua_event()
            input("\nTekan Enter untuk kembali...")

        elif pilih == '2':
            bersihkan_layar()
            print("\nEvent yang bisa diikuti:")
            ada_event = False
            for ev in events:
                if ev['status'] == 'ongoing':
                    print(f"ID {ev['id']} - {ev['nama']} ({ev['hadiah']})")
                    ada_event = True

            if not ada_event:
                print("Tidak ada event yang bisa diikuti.")
                input("\nTekan Enter...")
                continue

            id_pilih = cek_angka("Masukkan ID event: ", 1)
            event_dipilih = cari_event(id_pilih, "ongoing")

            if event_dipilih:
                if nama_user in event_dipilih['peserta']:
                    print("Kamu sudah terdaftar di event ini!")
                else:
                    event_dipilih['peserta'].append(nama_user)
                    print(f"Berhasil daftar ke {event_dipilih['nama']}!")
            else:
                print("Event tidak ditemukan.")
            input("\nTekan Enter...")

        elif pilih == '3':
            break
        else:
            print("Pilihan salah!")
            input("\nTekan Enter...")
