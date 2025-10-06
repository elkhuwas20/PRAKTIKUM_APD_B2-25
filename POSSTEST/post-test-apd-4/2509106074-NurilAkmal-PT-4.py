Nama_benar = "Nuril Akmal"
NIM_benar = 2509106074
pencobaan = 0
max_pencobaan = 3
while pencobaan < max_pencobaan:
    Nama = input("Masukkan Nama anda: ")
    NIM  = int(input("Masukkan NIM anda : "))
    if Nama == "Nuril Akmal" and NIM == 2509106074:
        print("Login berhasil. Selamat datang,", Nama)
        break
    pencobaan += 1
    if Nama == Nama_benar and NIM == NIM_benar:
        print("Akses diterima")
        break
    else:
        print("Nama atau NIM salah silahkan coba lagi sebanyak", max_pencobaan - pencobaan, "kali.")
else:
    print("Akses ditolak. Terlalu banyak percobaan.")
    exit()
print('===========Menu Pembelian Tiket============')
print('1. Tiket Regular (Harga: Rp 50.000)')
print('2. Tiket VIP     (Harga: Rp 100.000)')
print('3. Tiket VVIP   (Harga: Rp 150.000)')
pilihan = input('Pilih jenis tiket (1/2/3): ')
jumlah = int(input('Masukkan jumlah tiket yang dibeli: '))
if pilihan == '1':
        harga = 50000
        total_bayar = harga * jumlah
        print('Total pembayaran Tiket Regular: Rp', total_bayar)
elif pilihan == '2':
        harga = 100000
        total_bayar = harga * jumlah
        print('Total pembayaran Tiket VIP: Rp', total_bayar)
elif pilihan == '3':
        harga = 150000
        total_bayar = harga * jumlah
        print('Total pembayaran Tiket VVIP: Rp', total_bayar)
else:
     print('Pilihan tidak valid.')
if total_bayar >= 300000:
     diskon = total_bayar * 0.12
total_bayar = total_bayar - diskon
print('Anda mendapatkan diskon 12% sebesar: Rp', diskon)
print('Total pembayaran setelah diskon: Rp', total_bayar)
if total_bayar > 200000 and total_bayar <= 300000:
        cashback = total_bayar * 0.08
        print('Anda mendapatkan cashback 5% sebesar: Rp', cashback)
if total_bayar > 150000 and total_bayar <= 200000:
            print("Selamat Anda mendapatkan Poster Film Ekslusif")
else:
     print("Terima kasih telah memesan tiket di bioskop kami!")
print("========================================")

            
