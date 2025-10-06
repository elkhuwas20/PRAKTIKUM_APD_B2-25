ulangi = 10
for i in range (ulangi):
    print(f'Perulangan ke {i+1}')
simpan = [1, 'Dapupu', 4.00, True]
for i in simpan:
    print(i)
for i in range(1, 4):
    for j in range(1, 5):
        print(f'{i} x {j} = {i * j}')
print('')
for i in range(1, 4):
    for j in range(1, 5):
        if j == 3:
            continue
        print(f'{i} x {j} = {i * j}')
    print('')
for i in range(1, 12):
    for j in range(1, i+1):
        print("#", end=' ')
    print('')
print("Program Selesai")
print("========================================")
try:
    angka = int(input("Masukkan angka pembagi: "))
    hasil = 10 / angka
    print("Hasil pembagian 10 dengan", angka, "adalah", hasil)
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan.")
except ValueError:
    print("Error: Masukkan angka yang valid.")
except Exception as e:
    print("Terjadi kesalahan:", e)
except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")
finally:
    print("Terima kasih telah menggunakan program ini.")
print("========================================")
print("Program Selesai")
print("========================================")
  