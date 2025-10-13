for i in range(20):
    if i % 2 == 0:
        continue
    print("Angka ganjil:", i)
def cetak(a,b):
    for i in range(b):
        print(a, end= "")
    print()
cetak('@', 9)
cetak ('#', 13)

