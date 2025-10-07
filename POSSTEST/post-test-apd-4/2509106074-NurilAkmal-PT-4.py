Nama_benar = "Nuril Akmal"
NIM_benar = 2509106074
for percobaan in range(3):
    Nama = input("Masukkan Nama anda: ")
    NIM = int(input("Masukkan NIM anda: "))
    if Nama == Nama_benar and NIM == NIM_benar:
        print("Login berhasil. Selamat datang,", Nama)
        break
    else:
        print(f"Nama atau NIM salah. Sisa percobaan: {2 - percobaan}")
else:
    print("Akses ditolak. Terlalu banyak percobaan.")
    exit()
total_bayar = 0
jenis_tiket = ""
for _ in range(99999999999):
    print('\n===========Menu Pembelian Tiket============')
    print('1. Tiket Regular (Rp 50.000)')
    print('2. Tiket VIP     (Rp 100.000)')
    print('3. Tiket VVIP    (Rp 150.000)')
    print('4. Keluar')
    pilihan = input('Pilih jenis tiket (1/2/3/4): ')
    if pilihan == '4':
        break
    elif pilihan in ['1', '2', '3']:
        jumlah = int(input('Masukkan jumlah tiket: '))     
        if pilihan == '1':
            harga = 50000
            jenis_tiket = "Regular"
        elif pilihan == '2':
            harga = 100000
            jenis_tiket = "VIP"
        elif pilihan == '3':
            harga = 150000
            jenis_tiket = "VVIP" 
        subtotal = harga * jumlah
        total_bayar += subtotal
        print(f'\n{jumlah} tiket {jenis_tiket} = Rp {subtotal:,}')
        print(f'Total sementara: Rp {total_bayar:,}')
    else:
        print('Pilihan tidak valid!')
print('\n=========== TOTAL PEMBAYARAN ===========')
print(f'Total: Rp {total_bayar:,}')
if total_bayar >= 300000:
    diskon = total_bayar * 0.12
    total_akhir = total_bayar - diskon
    print(f'Diskon 12%: Rp {diskon:,}')
    print(f'Total bayar: Rp {total_akhir:,}')
elif total_bayar > 200000:
    cashback = total_bayar * 0.08
    print(f'Cashback 8%: Rp {cashback:,}')
    print(f'Total bayar: Rp {total_bayar:,}')
elif total_bayar > 150000:
    print(f'Total bayar: Rp {total_bayar:,}')
    print('Bonus: Poster Film Ekslusif')
else:
    print(f'Total bayar: Rp {total_bayar:,}')
print('Terima kasih telah memesan!')
print('=========================================')