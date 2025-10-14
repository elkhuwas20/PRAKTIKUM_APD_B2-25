import os
import sys
admin = ["Nuril Akmal", "Akmal Ganteng", "admin"]
daftaruser = ["Bang Pernanda", "Mba Triya", "pengguna"]
pwd_user = ["123", "321", "user123"]
password = ["123", "321", "admin123"]
events = [
    [1, "ETH Hackathon Samarinda", "10.000 USDT + NFT", "ongoing",  ["Team Alpha", "Team Beta"]],
    [2, "Solana DeFi Camp",        "5.000 USDT",        "finished", ["DeFi Ninjas"]],
]
data = {}
index = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*60)
    print("SISTEM MANAJEMEN EVENT WEB3 & HACKATHON".center(60))
    print("="*60)
    print("1. Login")
    print("2. Register")
    print("3. Lihat Event (Guest)")
    print("4. Keluar")
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan sistem ini.")

        sys.exit()
    elif pilihan == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        user = input("Masukkan username: ")
        pwd = input("Masukkan password: ")
        if user in daftaruser and pwd in pwd_user:
            if daftaruser.index(user) == pwd_user.index(pwd):
                print(f"Selamat datang, {user}!")
                input("Tekan Enter untuk melanjutkan...")
                continue
            else:
                print("Username dan password tidak sesuai.")
                input("Tekan Enter untuk mencoba lagi...")
                continue
    elif pilihan == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        nama_baru = input("Masukkan nama baru: ")
        if nama_baru in admin or nama_baru in daftaruser:
            print("Nama sudah terdaftar. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")
            continue
        pwd_baru = input("Masukkan password baru: ")
        daftaruser.append(nama_baru)
        pwd_user.append(pwd_baru)
        print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk melanjutkan...")
        continue
    elif pilihan == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nDaftar Event:")
        for event in events:
            print(f"ID: {event[0]}, Nama: {event[1]}, Hadiah: {event[2]}, Status: {event[3]}, Peserta: {', '.join(event[4])}")
        input("\nTekan Enter untuk kembali ke menu...")
        continue
    elif pilihan != '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opsi tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        continue  
    if user in admin and pwd in password:
        os.system('cls' if os.name == 'nt' else 'clear')
        if admin.index(user) == password.index(pwd):
            print(f"Selamat datang, {admin}!")
            while True:
                print("\nMenu:")
                print("1. Lihat Event")
                print("2. Create Event")
                print("3. Update Event")
                print("4. Delete Event")
                print("5. Kelola Peserta Event")
                print("6. Logout")
                choice = input("Pilih menu (1-6): ")
                if choice == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nDaftar Event:")
                    for event in events:
                        print(f"ID: {event[0]}, Nama: {event[1]}, Hadiah: {event[2]}, Status: {event[3]}, Peserta: {', '.join(event[4])}")
                    input("\nTekan Enter untuk kembali ke menu...")
                    
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    nama_event = input("Masukkan nama event: ")
                    hadiah_event = input("Masukkan hadiah event: ")
                    status_event = input("Masukkan status event (ongoing/finished): ")
                    events.append([len(events)+1, nama_event, hadiah_event, status_event, []])
                    print("Event berhasil ditambahkan!")
                    input("\nTekan Enter untuk kembali ke menu...")
                elif choice == '3':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    event_id = int(input("Masukkan ID event yang ingin diupdate: "))
                    for event in events:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if event[0] == event_id:
                            nama_event = input("Masukkan nama event baru: ")
                            hadiah_event = input("Masukkan hadiah event baru: ")
                            status_event = input("Masukkan status event baru (ongoing/finished): ")
                            event[1] = nama_event
                            event[2] = hadiah_event
                            event[3] = status_event
                            print("Event berhasil diupdate!")
                            break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Event dengan ID tersebut tidak ditemukan.")
                    input("\nTekan Enter untuk kembali ke menu...")
                elif choice == '4':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    event_id = int(input("Masukkan ID event yang ingin dihapus: "))
                    for event in events:
                        
                        if event[0] == event_id:
                            events.remove(event)
                            print("Event berhasil dihapus!")
                            break
                    else:
                        
                        print("Event dengan ID tersebut tidak ditemukan.")
                    input("\nTekan Enter untuk kembali ke menu...")
                elif choice == '5':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    event_id = int(input("Masukkan ID event untuk kelola peserta: "))
                    for event in events:
                        if event[0] == event_id:
                            print(f"Peserta saat ini: {', '.join(event[4]) if event[4] else 'Tidak ada peserta'}")
                            print("1. Tambah Peserta")
                            print("2. Hapus Peserta")
                            sub_choice = input("Pilih opsi (1-2): ")
                            if sub_choice == '1':
                                nama_peserta = input("Masukkan nama peserta: ")
                                event[4].append(nama_peserta)
                                print("Peserta berhasil ditambahkan!")
                            elif sub_choice == '2':
                                nama_peserta = input("Masukkan nama peserta yang ingin dihapus: ")
                                if nama_peserta in event[4]:
                                    event[4].remove(nama_peserta)
                                    print("Peserta berhasil dihapus!")
                                else:
                                    print("Peserta tidak ditemukan.")
                            else:
                                print("Opsi tidak valid.")
                            break
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Event dengan ID tersebut tidak ditemukan.")
                    input("\nTekan Enter untuk kembali ke menu...")
                elif choice == '6':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Logout berhasil.")
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Opsi tidak valid. Silakan coba lagi.")
                    input("\nTekan Enter untuk kembali ke menu...")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Username dan password tidak sesuai.")
            input("Tekan Enter untuk mencoba lagi...")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Username atau password salah.")
        input("Tekan Enter untuk mencoba lagi...")

