nama = input("Masukkan nama lengkap: ")
NIM = input("Masukkan NIM: ")
harga = int(input("Masukkan harga menu makanan: "))
print("========================================")
print( nama + " dengan NIM " + NIM + " ingin membeli makanan seharga Rp " + str(harga) )
print("========================================")
print("Daftar harga makanan dengan pajak:")
print("Pecel Lele  : Rp " + str(harga + harga*5/100) + " (pajak 5%)")
print("Mie Ayam    : Rp " + str(harga + harga*8/100) + " (pajak 8%)")
print("Nasi Padang : Rp " + str(harga + harga*10/100) + " (pajak 10%)")
print("========================================")
print("Terima kasih telah berkunjung, " + nama + "!")
print("========================================")



