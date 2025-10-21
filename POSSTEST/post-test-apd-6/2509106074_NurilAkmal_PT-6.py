import os
import sys

admin = {
    "Nuril Akmal": "admin123",
    "Akmal Ganteng": "admin123", 
    "admin": "admin123"
}

users = {
    "Bang Pernanda": "123",
    "Mba Triya": "321", 
    "pengguna": "user123"
}

events = [
    {
        "id": 1,
        "nama": "ETH Hackathon Samarinda", 
        "hadiah": "10.000 USDT + NFT",
        "status": "ongoing",
        "peserta": ["Team Alpha", "Team Beta"]
    },
    {
        "id": 2,
        "nama": "Solana DeFi Camp",
        "hadiah": "5.000 USDT", 
        "status": "finished",
        "peserta": ["DeFi Ninjas"]
    }
]

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
        
        # user biasa
        if user in users and users[user] == pwd:
            print(f"Selamat datang, {user}!")
            input("Tekan Enter untuk melanjutkan...")
            
            # Menu user biasa
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\nMenu Pengguna - {user}:")
                print("1. Lihat Event")
                print("2. Daftar Event")
                print("3. Logout")
                choice = input("Pilih menu (1-3): ")
                
                if choice == '1':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nDaftar Event:")
                    for event in events:
                        print(f"ID: {event['id']}, Nama: {event['nama']}, Hadiah: {event['hadiah']}, Status: {event['status']}, Peserta: {', '.join(event['peserta'])}")
                    input("\nTekan Enter untuk kembali ke menu...")
                
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nDaftar Event yang Tersedia:")
                    for event in events:
                        if event['status'] == "ongoing":
                            print(f"ID: {event['id']}, Nama: {event['nama']}, Hadiah: {event['hadiah']}")
                    
                    event_id = input("Masukkan ID event yang ingin diikuti: ")
                    
                    if event_id.isdigit():
                        event_id = int(event_id)
                        event_ditemukan = False
                        
                        for event in events:
                            if event['id'] == event_id and event['status'] == "ongoing":
                                event_ditemukan = True
                                if user not in event['peserta']:
                                    event['peserta'].append(user)
                                    print(f"Berhasil mendaftar ke event {event['nama']}!")
                                else:
                                    print("Anda sudah terdaftar di event ini.")
                                break
                        
                        if not event_ditemukan:
                            print("Event tidak ditemukan atau sudah selesai.")
                    else:
                        print("ID event harus berupa angka.")
                    
                    input("\nTekan Enter untuk kembali ke menu...")
                
                elif choice == '3':
                    print("Logout berhasil.")
                    break
                
                else:
                    print("Opsi tidak valid. Silakan coba lagi.")
                    input("\nTekan Enter untuk kembali ke menu...")
            continue
        
        # Cek login untuk admin
        elif user in admin and admin[user] == pwd:
            print(f"Selamat datang ADMIN, {user}!")
            input("Tekan Enter untuk melanjutkan...")
            
            # Menu untuk admin
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nMenu Admin:")
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
                        print(f"ID: {event['id']}, Nama: {event['nama']}, Hadiah: {event['hadiah']}, Status: {event['status']}, Peserta: {', '.join(event['peserta'])}")
                    input("\nTekan Enter untuk kembali ke menu...")
                
                elif choice == '2':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    nama_event = input("Masukkan nama event: ")
                    hadiah_event = input("Masukkan hadiah event: ")
                    
                    while True:
                        status_event = input("Masukkan status event (ongoing/finished): ").lower()
                        if status_event in ["ongoing", "finished"]:
                            break
                        else:
                            print("Status harus 'ongoing' atau 'finished'. Silakan coba lagi.")
                    
                    new_id = max(event['id'] for event in events) + 1 if events else 1
                    
                    events.append({
                        "id": new_id,
                        "nama": nama_event,
                        "hadiah": hadiah_event,
                        "status": status_event,
                        "peserta": []
                    })
                    print("Event berhasil ditambahkan!")
                    input("\nTekan Enter untuk kembali ke menu...")
                
                elif choice == '3':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    event_id = input("Masukkan ID event yang ingin diupdate: ")
                    
                    if event_id.isdigit():
                        event_id = int(event_id)
                        event_ditemukan = False
                        
                        for event in events:
                            if event['id'] == event_id:
                                event_ditemukan = True
                                nama_event = input("Masukkan nama event baru: ")
                                hadiah_event = input("Masukkan hadiah event baru: ")
                                
                                while True:
                                    status_event = input("Masukkan status event baru (ongoing/finished): ").lower()
                                    if status_event in ["ongoing", "finished"]:
                                        break
                                    else:
                                        print("Status harus 'ongoing' atau 'finished'. Silakan coba lagi.")
                                
                                event['nama'] = nama_event
                                event['hadiah'] = hadiah_event
                                event['status'] = status_event
                                print("Event berhasil diupdate!")
                                break
                        
                        if not event_ditemukan:
                            print("Event dengan ID tersebut tidak ditemukan.")
                    else:
                        print("ID event harus berupa angka.")
                    
                    input("\nTekan Enter untuk kembali ke menu...")
                
                elif choice == '4':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    event_id = input("Masukkan ID event yang ingin dihapus: ")
                    
                    if event_id.isdigit():
                        event_id = int(event_id)
                        event_ditemukan = False
                        
                        for event in events:
                            if event['id'] == event_id:
                                event_ditemukan = True
                                events.remove(event)
                                print("Event berhasil dihapus!")
                                break
                        
                        if not event_ditemukan:
                            print("Event dengan ID tersebut tidak ditemukan.")
                    else:
                        print("ID event harus berupa angka.")
                    
                    input("\nTekan Enter untuk kembali ke menu...")
                
                elif choice == '5':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    event_id = input("Masukkan ID event untuk kelola peserta: ")
                    
                    if event_id.isdigit():
                        event_id = int(event_id)
                        event_ditemukan = False
                        
                        for event in events:
                            if event['id'] == event_id:
                                event_ditemukan = True
                                print(f"Peserta saat ini: {', '.join(event['peserta']) if event['peserta'] else 'Tidak ada peserta'}")
                                print("1. Tambah Peserta")
                                print("2. Hapus Peserta")
                                sub_choice = input("Pilih opsi (1-2): ")
                                
                                if sub_choice == '1':
                                    nama_peserta = input("Masukkan nama peserta: ")
                                    event['peserta'].append(nama_peserta)
                                    print("Peserta berhasil ditambahkan!")
                                elif sub_choice == '2':
                                    nama_peserta = input("Masukkan nama peserta yang ingin dihapus: ")
                                    if nama_peserta in event['peserta']:
                                        event['peserta'].remove(nama_peserta)
                                        print("Peserta berhasil dihapus!")
                                    else:
                                        print("Peserta tidak ditemukan.")
                                else:
                                    print("Opsi tidak valid.")
                                break
                        
                        if not event_ditemukan:
                            print("Event dengan ID tersebut tidak ditemukan.")
                    else:
                        print("ID event harus berupa angka.")
                    
                    input("\nTekan Enter untuk kembali ke menu...")
                
                elif choice == '6':
                    print("Logout berhasil.")
                    break
                
                else:
                    print("Opsi tidak valid. Silakan coba lagi.")
                    input("\nTekan Enter untuk kembali ke menu...")
            continue
        
        # Jika login gagal
        print("Username atau password salah.")
        input("Tekan Enter untuk mencoba lagi...")
    
    elif pilihan == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        nama_baru = input("Masukkan nama baru: ")
        if nama_baru in admin or nama_baru in users:
            print("Nama sudah terdaftar. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")
            continue
        pwd_baru = input("Masukkan password baru: ")
        users[nama_baru] = pwd_baru
        print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk melanjutkan...")
        continue
    
    elif pilihan == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nDaftar Event:")
        for event in events:
            print(f"ID: {event['id']}, Nama: {event['nama']}, Hadiah: {event['hadiah']}, Status: {event['status']}, Peserta: {', '.join(event['peserta'])}")
        input("\nTekan Enter untuk kembali ke menu...")
        continue
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opsi tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")