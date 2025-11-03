# fungsi_event.py
from prettytable import PrettyTable
from data import events

def tampilkan_semua_event():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Event", "Hadiah", "Status", "Peserta"]

    if len(events) == 0:
        print("Tidak ada event.")
        return

    for ev in events:
        peserta_str = ", ".join(ev['peserta']) if ev['peserta'] else "Belum ada"
        table.add_row([ev['id'], ev['nama'], ev['hadiah'], ev['status'], peserta_str])

    print(table)
