# utils.py
import os
from data import events

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cek_angka(tulisan, minimal=1):
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
    for ev in events:
        if ev['id'] == id_event:
            if status_tertentu is None or ev['status'] == status_tertentu:
                return ev
    return None

def bikin_id_baru():
    if len(events) == 0:
        return 1
    return max(ev['id'] for ev in events) + 1

def hitung_peserta():
    total = 0
    for ev in events:
        total += len(ev['peserta'])
    return total
