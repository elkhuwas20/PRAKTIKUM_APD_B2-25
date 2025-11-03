# fungsi_admin.py
from data import events
from utils import bersihkan_layar, cek_angka, cari_event, bikin_id_baru
from fungsi_event import tampilkan_semua_event

def menu_admin(nama_admin):
    while True:
        bersihkan_layar()
        print(f"\nSelamat datang Admin {nama_admin}!")
        print("=" * 50)
        print("1. Lihat Event")
        print("2. Tambah Event")
        print("3. Edit Event")
        print("4. Hapus Event")
        print("5. Kelola Peserta")
        print("6. Logout")
        print("=" * 50)

        pilih = input("Pilih menu (1-6): ")

        if pilih == '1':
            tampilkan_semua_event()
            input("\nTekan Enter...")

        elif pilih == '2':
            nama = input("Nama event: ")
            hadiah = input("Hadiah: ")
            status = input("Status (ongoing/finished): ").lower()
            id_baru = bikin_id_baru()
            events.append({
                "id": id_baru,
                "nama": nama,
                "hadiah": hadiah,
                "status": status,
                "peserta": []
            })
            print("Event berhasil ditambah!")
            input("\nTekan Enter...")

        elif pilih == '3':
            tampilkan_semua_event()
            id_edit = cek_angka("Masukkan ID event: ")
            event_edit = cari_event(id_edit)
            if not event_edit:
                print("Event tidak ditemukan!")
            else:
                event_edit['nama'] = input("Nama baru: ") or event_edit['nama']
                event_edit['hadiah'] = input("Hadiah baru: ") or event_edit['hadiah']
                event_edit['status'] = input("Status baru: ") or event_edit['status']
                print("Event berhasil diupdate!")
            input("\nTekan Enter...")

        elif pilih == '4':
            tampilkan_semua_event()
            id_hapus = cek_angka("Masukkan ID event yang mau dihapus: ")
            event_hapus = cari_event(id_hapus)
            if event_hapus:
                events.remove(event_hapus)
                print("Event berhasil dihapus!")
            else:
                print("Event tidak ditemukan!")
            input("\nTekan Enter...")

        elif pilih == '5':
            tampilkan_semua_event()
            input("\nTekan Enter...")
        
        elif pilih == '6':
            break
        else:
            print("Pilihan salah!")
            input("\nTekan Enter...")
