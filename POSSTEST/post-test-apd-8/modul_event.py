from prettytable import PrettyTable

events = [
    [1, "ETH Hackathon Samarinda", "10.000 USDT + NFT", "ongoing", ["Team Alpha", "Team Beta"]],
    [2, "Solana DeFi Camp", "5.000 USDT", "finished", ["DeFi Ninjas"]],
]

def tampilkan_event():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Event", "Hadiah", "Status", "Peserta"]
    for event in events:
        table.add_row([event[0], event[1], event[2], event[3], ", ".join(event[4])])
    print(table)

def create_event(nama_event, hadiah_event, status_event):
    event_id = len(events) + 1
    events.append([event_id, nama_event, hadiah_event, status_event, []])

def update_event(event_id, nama_event, hadiah_event, status_event):
    for event in events:
        if event[0] == event_id:
            event[1] = nama_event
            event[2] = hadiah_event
            event[3] = status_event
            return True
    return False

def delete_event(event_id):
    for event in events:
        if event[0] == event_id:
            events.remove(event)
            return True
    return False

def daftar_peserta(event_id, peserta):
    for event in events:
        if event[0] == event_id:
            if peserta not in event[4]:
                event[4].append(peserta)
                return True
    return False
