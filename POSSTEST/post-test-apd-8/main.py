from modul_util import clear_screen, input_int
from modul_user import login, register
from modul_event import tampilkan_event, create_event, update_event, delete_event, daftar_peserta

while True:
    clear_screen()
    print("="*60)
    print("SISTEM MANAJEMEN EVENT WEB3 & HACKATHON".center(60))
    print("="*60)
    print("1. Login")
    print("2. Register")
    print("3. Lihat Event (Guest)")
    print("4. Keluar")
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == '4':
        clear_screen()
        print("Terima kasih telah menggunakan sistem ini.")
        break

    elif pilihan == '1':
        clear_screen()
        user = input("Masukkan username: ")
        pwd = input("Masukkan password: ")
        tipe_user = login(user, pwd)
        
        if tipe_user == "user":
            input("Login berhasil! Tekan Enter untuk melanjutkan...")
            while True:
                clear_screen()
                print(f"\nMenu Pengguna - {user}")
                print("1. Lihat Event")
                print("2. Daftar Event")
                print("3. Logout")
                choice = input("Pilih menu (1-3): ")

                if choice == '1':
                    clear_screen()
                    tampilkan_event()
                    input("Tekan Enter untuk kembali...")

                elif choice == '2':
                    clear_screen()
                    tampilkan_event()
                    event_id = input_int("Masukkan ID event yang ingin diikuti: ")
                    if daftar_peserta(event_id, user):
                        print("Berhasil mendaftar!")
                    else:
                        print("Gagal mendaftar. Event tidak ditemukan atau sudah selesai.")
                    input("Tekan Enter untuk kembali...")

                elif choice == '3':
                    break

        elif tipe_user == "admin":
            input("Login ADMIN berhasil! Tekan Enter untuk melanjutkan...")
            while True:
                clear_screen()
                print("\nMenu Admin")
                print("1. Lihat Event")
                print("2. Create Event")
                print("3. Update Event")
                print("4. Delete Event")
                print("5. Logout")
                choice = input("Pilih menu (1-5): ")

                if choice == '1':
                    clear_screen()
                    tampilkan_event()
                    input("Tekan Enter untuk kembali...")

                elif choice == '2':
                    clear_screen()
                    nama = input("Nama event: ")
                    hadiah = input("Hadiah event: ")
                    while True:
                        status = input("Status (ongoing/finished): ").lower()
                        if status in ["ongoing", "finished"]:
                            break
                        print("Status harus ongoing/finished.")
                    create_event(nama, hadiah, status)
                    print("Event berhasil dibuat!")
                    input("Tekan Enter untuk kembali...")

                elif choice == '3':
                    clear_screen()
                    event_id = input_int("Masukkan ID event: ")
                    nama = input("Nama event baru: ")
                    hadiah = input("Hadiah baru: ")
                    while True:
                        status = input("Status baru (ongoing/finished): ").lower()
                        if status in ["ongoing", "finished"]:
                            break
                        print("Status harus ongoing/finished.")
                    if update_event(event_id, nama, hadiah, status):
                        print("Update berhasil!")
                    else:
                        print("Event tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif choice == '4':
                    clear_screen()
                    event_id = input_int("Masukkan ID event yang ingin dihapus: ")
                    if delete_event(event_id):
                        print("Event berhasil dihapus!")
                    else:
                        print("Event tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif choice == '5':
                    break

        else:
            print("Username atau password salah.")
            input("Tekan Enter untuk mencoba lagi...")

    elif pilihan == '2':
        clear_screen()
        nama = input("Masukkan nama baru: ")
        pwd = input("Masukkan password baru: ")
        if register(nama, pwd):
            print("Registrasi berhasil! Silakan login.")
        else:
            print("Nama sudah terdaftar.")
        input("Tekan Enter untuk kembali...")

    elif pilihan == '3':
        clear_screen()
        tampilkan_event()
        input("Tekan Enter untuk kembali...")

    else:
        clear_screen()
        print("Opsi tidak valid.")
        input("Tekan Enter untuk melanjutkan...")
