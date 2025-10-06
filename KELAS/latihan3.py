kata = input("Masukkan sebuah kata: ")
huruf = input("Masukkan sebuah huruf: ")
for huruf in kata:
    if huruf in kata:
     print("Huruf", huruf, "ditemukan dalam kata", kata)
    break
else:
    print("Huruf", huruf, "tidak ditemukan dalam kata", kata)