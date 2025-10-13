hadir = False
if hadir:
    print("Hari ini ada kuliah kalkulus")
else:
    print("Kelas ditiadakan. Janji Zo")
for minggu in range(1, 5):
    print("Minggu", minggu, ":")
    print("Mahasiswa menunggu di kela")
    if minggu % 2 == 0:
        print("Pesan MT: 'Saya ada pr")
    else:
        print("Pesan MT: 'Kelas digan")
janji_MT = [
    "Kelas diganti lewat Zoom",
    "Materi akan dikirim lewat email",
    "Kuis akan dilakukan minggu depan",
    "Proyek luar kota sebentar lagi s"
]

for janji in janji_MT:
    print("Janji MT:", janji)
kenyataan = ("Jarang masuk kelas", "S")
print(kenyataan)
alasan = [
    "Proyek luar kota", "Acara keluar",
    "Kendala teknis Zoom", "Proyek lu"
]

print(set(alasan))