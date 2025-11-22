# 🚀 Quick Start Guide - Web3 Event Manager

Panduan cepat untuk memulai menggunakan aplikasi.

## ⚡ 5 Menit Setup

### Step 1: Buka File
1. Cari file `index.html` di folder project
2. Double-click atau drag ke browser
3. Atau gunakan **Live Server** (VS Code Extension)

### Step 2: Login Pertama Kali
**Sebagai User (Regular):**
- Username: `Bang Pernanda`
- Password: `123`

**Sebagai Admin:**
- Username: `Nuril Akmal`
- Password: `123`

### Step 3: Explore Fitur
- Lihat event yang tersedia
- Daftar ke event yang diinginkan
- Lihat statistik di dashboard

---

## 🎯 Panduan Per Peran

### 👤 User (Regular)

#### Login
```
1. Klik "Login Sekarang" atau menu "Login"
2. Masukkan username & password
3. Tekan tombol "Login"
```

#### Lihat Event
```
1. Klik "Events" di navbar
2. Scroll untuk melihat semua event
3. Baca info: hadiah, status, peserta
```

#### Daftar Event
```
1. Lihat event yang diinginkan
2. Klik tombol "Daftar"
3. Notifikasi sukses akan muncul
4. Event muncul di "My Events"
```

#### Lihat Dashboard
```
1. Setelah login, otomatis di dashboard
2. Lihat statistik di atas
3. Scroll untuk lihat recent events
```

#### My Events
```
1. Klik "My Events" di sidebar
2. Lihat semua event yang sudah didaftar
3. Klik untuk lihat detail
```

---

### 🔐 Admin

#### Login Admin
```
1. Klik "Login"
2. Gunakan akun admin
3. Tekan "Login"
4. Menu admin akan muncul di sidebar
```

#### Membuat Event Baru
```
1. Di dashboard, klik "Create Event"
2. Isi semua field:
   - Event Name
   - Prize Pool
   - Status (ongoing/finished)
   - Description (optional)
3. Klik "Create Event"
```

#### Edit Event
```
1. Di dashboard, lihat event di tabel
2. Klik tombol "Edit"
3. Modal akan terbuka
4. Ubah data sesuai kebutuhan
5. Klik "Update"
```

#### Hapus Event
```
1. Klik tombol "Edit" pada event
2. Modal akan terbuka
3. Klik tombol "Delete"
4. Konfirmasi penghapusan
5. Event akan dihapus
```

#### Lihat Statistik
```
1. Dashboard sudah menampilkan stats
2. Total Events, Registered Users, dll
3. Lihat table dengan detail setiap event
```

---

## 📱 Fitur-Fitur Utama

### 1. Authentication System
- Register akun baru
- Login dengan credentials
- Automatic session management
- Logout dengan aman

### 2. Event Management
- Buat event baru (admin)
- Edit event (admin)
- Hapus event (admin)
- Lihat detail event

### 3. Registration System
- Daftar event sebagai user
- Lihat peserta event
- Status event (ongoing/finished)
- Statistik peserta

### 4. Dashboard
- Statistik overview
- Recent events
- My events
- Event management (admin)

### 5. Advanced Features
- Data backup & restore
- Event search & filter
- Activity tracking
- Performance monitoring
- Data export (CSV/JSON)

---

## 💡 Tips & Tricks

### Tip 1: Test Multiple Accounts
Coba switch between user dan admin accounts untuk test fitur berbeda.

### Tip 2: Buat Event Test
Sebagai admin, buat beberapa event untuk test, lalu daftar sebagai user.

### Tip 3: Gunakan Console
Tekan `F12` untuk buka Developer Tools, bisa test API di console:
```javascript
// Test search
Utilities.Search.searchByName('Hackathon');

// Test stats
Utilities.Analytics.getAllStats();

// Test activity
Utilities.Activity.getActivityReport();
```

### Tip 4: Backup Data
Jangan lupa backup data menggunakan fitur backup, atau export sebagai JSON/CSV.

### Tip 5: Responsif Design
Aplikasi bisa dibuka di mobile, tablet, atau desktop. Coba resize browser!

---

## 🔄 Workflow Examples

### Workflow 1: User Baru Mendaftar & Ikut Event
```
1. Click "Register"
2. Isi username & password baru
3. Click "Register"
4. Kembali ke "Login" tab
5. Login dengan akun baru
6. Lihat event yang tersedia
7. Klik "Daftar" pada event yang diinginkan
8. Lihat di "My Events"
```

### Workflow 2: Admin Membuat Event
```
1. Login sebagai admin
2. Di dashboard, klik "Create Event"
3. Isi detail event:
   - Name: "Polygon DeFi Hack 2024"
   - Prize: "25.000 USDT + NFT"
   - Status: "ongoing"
   - Description: "Kompetisi DeFi terbesar di Polygon"
4. Klik "Create Event"
5. Event muncul di list
```

### Workflow 3: User Lihat Event & Daftar
```
1. Jangan perlu login, bisa langsung lihat events
2. Klik menu "Events"
3. Lihat semua event tersedia
4. Untuk daftar, klik tombol "Login untuk daftar"
5. Setelah login, daftar bisa dilakukan
6. Klik "Daftar"
7. Cek di "My Events"
```

---

## ❓ FAQ

### Q: Berapa akun yang bisa dibuat?
A: Unlimited. User bisa register sebanyak mungkin dengan username unik.

### Q: Apakah data tersimpan permanen?
A: Saat ini data disimpan di memory browser. Untuk persistensi, gunakan localStorage atau backend.

### Q: Bagaimana cara backup data?
A: Di console, jalankan: `Utilities.Storage.exportData()`

### Q: Bisa switch role dari user jadi admin?
A: Tidak. Hanya bisa login dengan akun yang sudah terdefinisi. Untuk test, gunakan akun admin yang ada.

### Q: Event bisa didaftar berapa kali?
A: Satu user hanya bisa daftar 1 kali per event.

### Q: Apa bedanya ongoing dan finished?
A: **Ongoing** = event sedang berlangsung, bisa daftar
   **Finished** = event sudah selesai, tidak bisa daftar

### Q: Data hilang setelah refresh browser?
A: Ya, kecuali sudah implement localStorage atau backend.

### Q: Bisa add custom field di event?
A: Bisa, edit di `app.js` bagian event object structure.

---

## 🎨 Customization Quick Tips

### Ubah Warna Tema
1. Buka `styles.css`
2. Cari section `:root`
3. Ubah hex color, contoh: `--primary-color: #FF0000;`

### Ubah Title Website
1. Buka `index.html`
2. Cari `<title>Web3 Event Manager...</title>`
3. Ganti dengan title baru

### Ubah Logo
1. Di navbar, ubah icon dari Font Awesome
2. Atau ganti text "Web3Events" dengan nama lain

### Ubah Default Event
1. Buka `app.js`
2. Cari `appData.events = [...]`
3. Edit atau tambah event

---

## 🚨 Troubleshooting

### Problem: "Fitur tidak berfungsi"
**Solution:**
1. Refresh browser (Ctrl+F5)
2. Clear cache browser
3. Buka console (F12), cek error
4. Pastikan semua file loaded (.html, .css, .js)

### Problem: "Login gagal"
**Solution:**
1. Pastikan username & password benar (case-sensitive)
2. Username harus: `Bang Pernanda`, `Mba Triya`, `Nuril Akmal`, atau `Akmal Ganteng`
3. Password: `123`, `321`, atau `admin123`

### Problem: "Event tidak muncul"
**Solution:**
1. Refresh halaman
2. Pastikan event sudah dibuat
3. Klik "Events" di navbar
4. Check console untuk error

### Problem: "Data hilang saat refresh"
**Solution:**
Ini normal! Data disimpan di memory saja. Untuk fix:
1. Implementasikan localStorage
2. Atau gunakan backend/database

### Problem: "Tombol tidak responsive"
**Solution:**
1. Clear browser cache
2. Update browser ke versi terbaru
3. Cek console untuk JavaScript error

---

## 📚 Next Steps

### Level 1: Basic Usage (Sekarang)
- ✅ Login/Register
- ✅ Lihat event
- ✅ Daftar event

### Level 2: Advanced Usage
- 📊 Gunakan Analytics
- 🔍 Gunakan Search
- 💾 Backup & Restore data
- 📊 Export data

### Level 3: Customization
- 🎨 Ubah tema warna
- 🔧 Tambah field custom
- 📝 Integrasikan dengan database
- 🚀 Deploy ke server

### Level 4: Integration
- 🔌 Backend API integration
- 🗄️ Database connection
- 📧 Email notifications
- 💳 Payment gateway

---

## 📞 Support & Resources

- **Developer**: Nuril Akmal (2509106074)
- **Project**: PRAKTIKUM APD B2 - Event Management System
- **Repository**: GitHub PRAKTIKUM_APD_B2-25

---

**Happy coding! 🚀**

Jika ada pertanyaan atau butuh bantuan, silakan refer ke dokumentasi lengkap di `README.md` atau `API_GUIDE.md`.
