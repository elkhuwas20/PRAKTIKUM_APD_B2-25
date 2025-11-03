# # # # from math import sqrt
# # # # from math import factorial
# # # # nama = []
# # # # usia = []
# # # # prodi = []
# # # # def input_data():
# # # #     n = int(input("Masukkan jumlah data yang akan diinput: "))
# # # #     for i in range(n):
# # # #         nama.append(input(f"Masukkan nama ke-{i+1}: "))
# # # #         usia.append(int(input(f"Masukkan usia{i+1}: ")))
# # # #         prodi.append(input(f"Masukkan prodi ke-{i+1}: "))
# # # # def tampil_data():
# # # #     print("\nData Mahasiswa:")
# # # #     for i in range(len(nama)):
# # # #         print(f"Nama: {nama[i]},Usia: {usia[i]} Tahun, Prodi: {prodi[i]}")
# # # # input_data()
# # # # tampil_data()
# # # # print("========================================")
# # # # print("Program Selesai")
# # # # def hitung_statistik(data):
# # # #     n = len(data)
# # # #     mean = sum(data) / n
# # # #     variance = sum((x - mean) ** 2 for x in data) / n
# # # #     std_dev = sqrt(variance)
# # # #     return mean, variance, std_dev
# # # # data_angka = [10, 20, 30, 40, 50]
# # # # import random

# # # # data = ['pisang', 'apel', 'jeruk', 'mangga', 'anggur']
# # # # acak = []
# # # # for i in range(3):
# # # #     acak.append(random.choice(data))
# # # # print("Buah acak yang dipilih:", acak)
# # # import random
# # # print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
# # # pilih_acak = ["pisang", "rambutan", "manggis"]
# # # acak = "apcb"
# # # print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# # # print(random.choice(acak)) # memilih 1 karakter acak pada string
# # # # memasukkan satu persatu nilai dari kumpulan_angka
# # # # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# # # kumpulan_angka = "1234567890"
# # # hasil = ""
# # # for i in range(4):
# # #     hasil += random.choice(kumpulan_angka)
# # # print(hasil)

# # # acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# # # random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang sudah diacak
# # # print(acak_kartu)
# # import inquirer
# # # deklarasi struktur dictionary
# # data = {
# # 'nama': [],
# # 'nim': [],
# # 'no_hp': []
# # }
# # def tambahData():
# #     questions = [
# # inquirer.Text('nama', message="Input nama mu"),
# # inquirer.Text('nim', message="Input NIM kamu"),
# # inquirer.Text('no_hp', message="Input nomor hp kamu",)]
# #     answers = inquirer.prompt(questions)
# #     print("Data berhasil ditambahkan!")
# # # hasil dari semua input diatas adalah:
# # # {'name': 'nilai dari input name', 'nim': 'nilai dari input nim', 'no_hp': 'nilai dari input no_hp'}
# # #  # hasil input akan disimpan kedalam variabel answer
# # # tambahkan isi dari list, sesuai key nya masing-masing
# # data['nama'].append(answers['nama'])
# # data['nim'].append(answers['nim'])
# # data['no_hp'].append(answers['no_hp'])
# # # panggil fungsi
# # tambahData()
# # # contoh jika ingin melihat isi dari dictionary data dengan key 'nama'
# # print(f"List nama:")
# # for i, nama in enumerate(data['nama']):
# #     print(f"{i+1}. {nama}")
# import inquirer
# # deklarasi struktur dictionary
# data = {
# 'nama': [],
# 'nim': [],
# 'no_hp': []
# }
# def tambahData():
#     questions = [
#     inquirer.Text('nama', message="Input nama mu"),
#     inquirer.Text('nim', message="Input NIM kamu"),
#     inquirer.Text('no_hp', message="Input nomor hp kamu",)]
#     # hasil dari semua input diatas adalah:
#     # {'name': 'nilai dari input name', 'nim': 'nilai dari input nim','no_hp': 'nilai input no_hp'}]
# answers = inquirer.prompt # hasil input akan disimpan kedalam variabel answer
# # tambahkan isi dari list, sesuai key nya masing-masing
# data['nama'].append(answers['nama'])
# data['nim'].append(answers['nim'])
# data['no_hp'].append(answers['no_hp'])
# # panggil fungsi
# tambahData()
# # contoh jika ingin melihat isi dari dictionary data dengan key 'nama'
# print(f"List nama:")
# for i, nama in enumerate(data['nama']):
#     print(f"{i+1}. {nama}")
import inquirer
pertanyaan = [
inquirer.List(
'size',
message="What size do you need?",
choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
),
] 
# mendapatkan jawaban
answer = inquirer.prompt(pertanyaan)
print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
print(answer['size']) # Ambil nilai dari key 'size'
