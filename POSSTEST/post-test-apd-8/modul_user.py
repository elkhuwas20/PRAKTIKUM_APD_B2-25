# modul_user.py
admin = ["Nuril Akmal", "Akmal Ganteng", "admin"]
password_admin = ["123", "321", "admin123"]
daftar_user = ["Bang Pernanda", "Mba Triya", "pengguna"]
password_user = ["123", "321", "user123"]

def login(user, pwd):
    if user in daftar_user:
        index = daftar_user.index(user)
        if pwd == password_user[index]:
            return "user"
    elif user in admin:
        index = admin.index(user)
        if pwd == password_admin[index]:
            return "admin"
    return None

def register(nama_baru, pwd_baru):
    if nama_baru in admin or nama_baru in daftar_user:
        return False
    daftar_user.append(nama_baru)
    password_user.append(pwd_baru)
    return True
