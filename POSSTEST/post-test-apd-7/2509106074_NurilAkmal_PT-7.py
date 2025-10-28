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
def cek_angka(tulisan, minimal=1):
    """Fungsi untuk cek apakah input adalah angka yang benar"""
    while True:
        try:
            angka_input = input(tulisan)  
            angka = int(angka_input)  
            
            if angka < minimal:
                print(f"Angka harus minimal {minimal}")
                continue
            
            return angka
        except:
            print("Salah! Harus input angka.")
def cari_event(id_event, status_tertentu=None):
    """Fungsi untuk mencari event berdasarkan ID"""
    try:
        for ev in events:
            if ev['id'] == id_event:
                if status_tertentu == None or ev['status'] == status_tertentu:
                    return ev
        return None
    except:
        print("Error saat cari event")
        return None
def bikin_id_baru():
    """Fungsi untuk bikin ID event baru"""
    try:
        if len(events) == 0:
            return 1
        
        id_terbesar = 0 
        for ev in events:
            if ev['id'] > id_terbesar:
                id_terbesar = ev['id']
        
        return id_terbesar + 1
    except:
        print("Error bikin ID")
        return 1
def hitung_peserta():
    """Fungsi rekursif untuk hitung total peserta semua event"""
    
    def hitung_rekursif(daftar_event, posisi):
        if posisi >= len(daftar_event):
            return 0
        jumlah = len(daftar_event[posisi]['peserta'])  
        return jumlah + hitung_rekursif(daftar_event, posisi + 1)
    try:
        return hitung_rekursif(events, 0)
    except:
        print("Error hitung peserta")
        return 0
def bersihkan_layar():
    """Prosedur untuk bersihkan layar"""
    os.system('cls' if os.name == 'nt' else 'clear')
def tampilkan_semua_event():
    """Prosedur untuk tampilkan semua event"""
    try:
        print("\nDaftar Event:")
        print("=" * 80)
        
        if len(events) == 0:
            print("Tidak ada event")
            return
        
        for ev in events:
            print(f"ID: {ev['id']}")
            print(f"Nama: {ev['nama']}")
            print(f"Hadiah: {ev['hadiah']}")
            print(f"Status: {ev['status']}")
            
            if len(ev['peserta']) > 0:
                print(f"Peserta: {', '.join(ev['peserta'])}")
            else:
                print("Peserta: Belum ada")
            
            print("-" * 80)
    except:
        print("Error tampilkan event")


# ===== MENU USER BIASA =====
def menu_user(nama_user):
    """Menu untuk user biasa"""
    
    while True:
        bersihkan_layar()
        print(f"\nSelamat datang, {nama_user}!")
        print("=" * 60)
        print("1. Lihat Event")
        print("2. Daftar Event")
        print("3. Logout")
        print("=" * 60)
        
        pilih = input("Pilih menu (1-3): ")
        
        # Menu 1: Lihat event
        if pilih == '1':
            bersihkan_layar()
            tampilkan_semua_event()
            input("\nTekan Enter untuk kembali...")
        
        # Menu 2: Daftar event
        elif pilih == '2':
            bersihkan_layar()
            print("\nEvent yang bisa diikuti:")
            print("-" * 60)
            
            # Cari event yang ongoing
            ada_event = False
            for ev in events:
                if ev['status'] == 'ongoing':
                    ada_event = True
                    print(f"ID: {ev['id']}, Nama: {ev['nama']}, Hadiah: {ev['hadiah']}")
            
            if not ada_event:
                print("Tidak ada event yang bisa diikuti")
                input("\nTekan Enter untuk kembali...")
                continue
            
            print("-" * 60)
            
            try:
                id_pilih = cek_angka("Masukkan ID event (0 untuk batal): ", 0)
                
                if id_pilih == 0:
                    continue
                
                event_dipilih = cari_event(id_pilih, "ongoing")
                
                if event_dipilih != None:
                    if nama_user in event_dipilih['peserta']:
                        print("Kamu sudah terdaftar di event ini!")
                    else:
                        event_dipilih['peserta'].append(nama_user)
                        print(f"Berhasil daftar ke event {event_dipilih['nama']}!")
                else:
                    print("Event tidak ditemukan atau sudah selesai")
            except:
                print("Terjadi error")
            
            input("\nTekan Enter untuk kembali...")
        
        # Menu 3: Logout
        elif pilih == '3':
            print("Logout berhasil")
            input("\nTekan Enter...")
            break
        
        else:
            print("Pilihan salah!")
            input("\nTekan Enter...")
# ===== MENU ADMIN =====
def menu_admin(nama_admin):
    """Menu untuk admin"""
    
    while True:
        bersihkan_layar()
        print(f"\nSelamat datang Admin {nama_admin}!")
        print("=" * 60)
        print("1. Lihat Event")
        print("2. Tambah Event")
        print("3. Edit Event")
        print("4. Hapus Event")
        print("5. Kelola Peserta")
        print("6. Logout")
        print("=" * 60)
        
        pilih = input("Pilih menu (1-7): ")
        
        # Menu 1: Lihat event
        if pilih == '1':
            bersihkan_layar()
            tampilkan_semua_event()
            input("\nTekan Enter untuk kembali...")
        
        # Menu 2: Tambah event
        elif pilih == '2':
            bersihkan_layar()
            print("\n=== TAMBAH EVENT BARU ===")
            
            try:
                nama = input("Nama event: ")
                if nama == "":
                    print("Nama tidak boleh kosong!")
                    input("\nTekan Enter...")
                    continue
                
                hadiah = input("Hadiah event: ")
                if hadiah == "":
                    print("Hadiah tidak boleh kosong!")
                    input("\nTekan Enter...")
                    continue
                
                while True:
                    status = input("Status (ongoing/finished): ").lower()
                    if status == "ongoing" or status == "finished":
                        break
                    else:
                        print("Status harus ongoing atau finished!")
                
                id_baru = bikin_id_baru()
                
                events.append({
                    "id": id_baru,
                    "nama": nama,
                    "hadiah": hadiah,
                    "status": status,
                    "peserta": []
                })
                
                print(f"\nEvent berhasil ditambahkan dengan ID {id_baru}!")
            except:
                print("Terjadi error saat tambah event")
            
            input("\nTekan Enter...")       
        # Menu 3: Edit event
        elif pilih == '3':
            bersihkan_layar()
            tampilkan_semua_event()
            
            try:
                id_edit = cek_angka("\nMasukkan ID event yang mau diedit (0 untuk batal): ", 0)
                
                if id_edit == 0:
                    continue
                
                event_edit = cari_event(id_edit)
                
                if event_edit != None:
                    print(f"\nEvent sekarang: {event_edit['nama']}")
                    
                    nama_baru = input("Nama baru: ")
                    hadiah_baru = input("Hadiah baru: ")
                    
                    while True:
                        status_baru = input("Status baru (ongoing/finished): ").lower()
                        if status_baru == "ongoing" or status_baru == "finished":
                            break
                        else:
                            print("Status harus ongoing atau finished!")
                    
                    if nama_baru != "":
                        event_edit['nama'] = nama_baru
                    if hadiah_baru != "":
                        event_edit['hadiah'] = hadiah_baru
                    event_edit['status'] = status_baru
                    
                    print("\nEvent berhasil diedit!")
                else:
                    print("\nEvent tidak ditemukan!")
            except:
                print("Terjadi error saat edit event")
            
            input("\nTekan Enter...")
        
        # Menu 4: Hapus event
        elif pilih == '4':
            bersihkan_layar()
            tampilkan_semua_event()
            
            try:
                id_hapus = cek_angka("\nMasukkan ID event yang mau dihapus (0 untuk batal): ", 0)
                
                if id_hapus == 0:
                    continue
                
                event_hapus = cari_event(id_hapus)
                
                if event_hapus != None:
                    konfirmasi = input(f"Yakin mau hapus '{event_hapus['nama']}'? (y/n): ")
                    if konfirmasi.lower() == 'y':
                        events.remove(event_hapus)
                        print("\nEvent berhasil dihapus!")
                    else:
                        print("\nBatal hapus event")
                else:
                    print("\nEvent tidak ditemukan!")
            except:
                print("Terjadi error saat hapus event")
            
            input("\nTekan Enter...")
        
        # Menu 5: Kelola peserta
        elif pilih == '5':
            bersihkan_layar()
            tampilkan_semua_event()
            
            try:
                id_peserta = cek_angka("\nMasukkan ID event (0 untuk batal): ", 0)
                
                if id_peserta == 0:
                    continue
                
                event_peserta = cari_event(id_peserta)
                
                if event_peserta != None:
                    print(f"\nEvent: {event_peserta['nama']}")
                    if len(event_peserta['peserta']) > 0:
                        print(f"Peserta sekarang: {', '.join(event_peserta['peserta'])}")
                    else:
                        print("Peserta sekarang: Belum ada")
                    
                    print("\n1. Tambah Peserta")
                    print("2. Hapus Peserta")
                    sub = input("Pilih (1-2): ")
                    
                    if sub == '1':
                        nama_peserta = input("Nama peserta: ")
                        if nama_peserta != "":
                            if nama_peserta not in event_peserta['peserta']:
                                event_peserta['peserta'].append(nama_peserta)
                                print(f"Peserta {nama_peserta} berhasil ditambah!")
                            else:
                                print("Peserta sudah terdaftar!")
                        else:
                            print("Nama tidak boleh kosong!")
                    
                    elif sub == '2':
                        nama_peserta = input("Nama peserta yang mau dihapus: ")
                        if nama_peserta in event_peserta['peserta']:
                            event_peserta['peserta'].remove(nama_peserta)
                            print(f"Peserta {nama_peserta} berhasil dihapus!")
                        else:
                            print("Peserta tidak ditemukan!")
                    else:
                        print("Pilihan salah!")
                else:
                    print("\nEvent tidak ditemukan!")
            except:
                print("Terjadi error")
            
            input("\nTekan Enter...")
        # Menu 6: Logout
        elif pilih == '6':
            print("Logout berhasil")
            input("\nTekan Enter...")
            break
        
        else:
            print("Pilihan salah!")
            input("\nTekan Enter...")


# ===== PROGRAM UTAMA =====
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
    
    # Menu 1: Login
    if pilihan == '1':
        bersihkan_layar()
        print("=== LOGIN ===\n")
        
        try:
            user = input("Username: ")
            pwd = input("Password: ")
            
            # Cek user biasa
            if user in users and users[user] == pwd:
                print(f"\nLogin berhasil! Selamat datang {user}!")
                input("Tekan Enter...")
                menu_user(user)
            
            # Cek admin
            elif user in admin and admin[user] == pwd:
                print(f"\nLogin berhasil! Selamat datang Admin {user}!")
                input("Tekan Enter...")
                menu_admin(user)
            
            # Login gagal
            else:
                print("\nUsername atau password salah!")
                input("Tekan Enter...")
        except:
            print("Terjadi error saat login")
            input("Tekan Enter...")
    
    # Menu 2: Register
    elif pilihan == '2':
        bersihkan_layar()
        print("=== REGISTER USER BARU ===\n")
        
        try:
            nama_baru = input("Username baru: ")
            
            if nama_baru == "":
                print("Username tidak boleh kosong!")
                input("Tekan Enter...")
                continue
            
            if nama_baru in admin or nama_baru in users:
                print("Username sudah dipakai! Coba yang lain.")
                input("Tekan Enter...")
                continue
            
            pwd_baru = input("Password baru: ")
            
            if pwd_baru == "":
                print("Password tidak boleh kosong!")
                input("Tekan Enter...")
                continue
            
            if len(pwd_baru) < 3:
                print("Password minimal 3 karakter!")
                input("Tekan Enter...")
                continue
            
            users[nama_baru] = pwd_baru
            print(f"\nRegistrasi berhasil! Silakan login dengan username '{nama_baru}'")
            input("Tekan Enter...")
        except:
            print("Terjadi error saat register")
            input("Tekan Enter...")
    
    # Menu 3: Lihat event sebagai guest
    elif pilihan == '3':
        bersihkan_layar()
        tampilkan_semua_event()
        
        try:
            total_peserta = hitung_peserta()
            print(f"\nTotal peserta di semua event: {total_peserta}")
        except:
            print("Error hitung peserta")
        
        input("\nTekan Enter...")
    
    # Menu 4: Keluar
    elif pilihan == '4':
        bersihkan_layar()
        print("Terima kasih sudah pakai sistem ini!")
        print("Sampai jumpa!")
        sys.exit()
    
    else:
        print("\nPilihan salah! Coba lagi.")
        input("Tekan Enter...")