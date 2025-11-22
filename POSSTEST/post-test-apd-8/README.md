# Web3 Event Manager - Event Management System

Sistem manajemen event Web3 dan Hackathon dengan desain modern dan responsif.

## 🚀 Fitur Utama

### Untuk Pengguna (User)
- ✅ Login & Register
- 📋 Melihat semua event yang tersedia
- 📝 Mendaftar ke event
- 📊 Dashboard dengan statistik
- 📌 Melihat event yang sudah didaftar

### Untuk Admin
- 🔧 Semua fitur pengguna
- ➕ Membuat event baru
- ✏️ Mengubah data event
- 🗑️ Menghapus event
- 👥 Melihat list peserta

## 📱 Teknologi yang Digunakan

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Design Pattern**: Web3/Modern UI
- **Storage**: LocalStorage (dapat diubah ke backend)
- **Icons**: Font Awesome 6
- **Responsive**: Mobile-first design

## 🎨 Desain Features

- Dark theme dengan gradient Web3
- Animasi smooth dan professional
- Glassmorphism effects
- Responsive design untuk semua device
- Modern gradient buttons
- Interactive cards dengan hover effects

## 🔐 Akun Demo

### User Accounts
```
Username: Bang Pernanda
Password: 123

Username: Mba Triya
Password: 321
```

### Admin Accounts
```
Username: Nuril Akmal
Password: 123

Username: Akmal Ganteng
Password: 321
```

## 📂 Struktur File

```
post-test-apd-8/
├── index.html          # File HTML utama
├── styles.css          # Styling CSS
├── app.js             # Logic JavaScript
├── README.md          # Dokumentasi
└── 2509106074_NurilAkmal/
    ├── main.py        # Python backend (original)
    ├── modul_event.py # Module event Python
    ├── modul_user.py  # Module user Python
    └── modul_util.py  # Module utility Python
```

## 🚀 Cara Menggunakan

### 1. Buka Aplikasi
- Buka file `index.html` di browser
- Atau gunakan Live Server di VS Code

### 2. Navigasi
- **Home**: Halaman awal dengan hero section
- **Login**: Login/Register akun
- **Events**: Lihat semua event (tanpa harus login)
- **Dashboard**: Area khusus setelah login

### 3. Fitur User
1. Login dengan akun user
2. Klik "Events" atau "My Events" di dashboard
3. Klik tombol "Daftar" pada event yang diminati
4. Lihat event Anda di "My Events"

### 4. Fitur Admin
1. Login dengan akun admin
2. Gunakan menu "Create Event" untuk membuat event baru
3. Edit atau hapus event melalui dashboard
4. Lihat statistik di halaman dashboard

## 🎯 Alur Event

### State Event
- **Ongoing**: Event sedang berlangsung, peserta bisa daftar
- **Finished**: Event sudah selesai, peserta tidak bisa daftar

### Peserta
- Satu user bisa mendaftar multiple events
- User tidak bisa mendaftar event yang sudah finished
- Tidak ada duplikasi pendaftaran untuk event yang sama

## 💾 Data Persistence

Data saat ini disimpan dalam memory (hilang setelah refresh). Untuk persistensi:

### Option 1: LocalStorage (Browser)
```javascript
// Di app.js, tambahkan sebelum closebutton di navigateTo('home')
localStorage.setItem('appData', JSON.stringify(appData));
```

### Option 2: Backend Server
Integrasikan dengan:
- Node.js + Express
- Python Flask/Django
- PHP Laravel
- Database: MySQL, PostgreSQL, MongoDB

## 🔧 Customization

### Mengubah Warna
Edit variabel CSS di `styles.css`:
```css
:root {
    --primary-color: #6366f1;  /* Ubah warna utama */
    --secondary-color: #8b5cf6;
    --tertiary-color: #ec4899;
    --danger-color: #ef4444;
}
```

### Menambah Event Default
Di `app.js`, tambah ke `appData.events`:
```javascript
{
    id: 3,
    name: "Polkadot Summit 2024",
    prize: "20.000 USDT",
    status: "ongoing",
    participants: [],
    description: "Konferensi Polkadot terbesar di Asia Tenggara"
}
```

### Menambah User Default
Di `app.js`, tambah ke `appData.users`:
```javascript
{
    username: "username_baru",
    password: "password123",
    type: "user"  // atau "admin"
}
```

## 📊 Struktur Data Event

```javascript
{
    id: 1,                           // ID unik
    name: "ETH Hackathon",           // Nama event
    prize: "10.000 USDT + NFT",     // Hadiah
    status: "ongoing",               // Status: ongoing/finished
    participants: ["User1", "User2"], // List peserta
    description: "Deskripsi event"   // Deskripsi
}
```

## 📊 Struktur Data User

```javascript
{
    username: "username",    // Username unik
    password: "password",    // Password (simple hash recommended)
    type: "user"            // Type: user/admin
}
```

## 🛣️ Roadmap Fitur

- [ ] Backend integration (Node.js/Python)
- [ ] Database persistence
- [ ] Email verification
- [ ] Event search & filter
- [ ] Event categories
- [ ] User profile page
- [ ] Event reviews & ratings
- [ ] Payment integration
- [ ] QR code check-in
- [ ] Notification system

## 🔐 Security Notes

⚠️ **Catatan Keamanan:**
- Password saat ini disimpan plain text (JANGAN gunakan untuk production)
- Untuk production, gunakan:
  - Password hashing (bcrypt, argon2)
  - JWT authentication
  - HTTPS/SSL
  - Input validation & sanitization
  - CSRF protection

## 🐛 Troubleshooting

### Fitur tidak berfungsi
- Buka Browser Developer Tools (F12)
- Cek console untuk error messages
- Clear browser cache (Ctrl+Shift+Delete)

### Data hilang setelah refresh
- Data disimpan dalam memory saja
- Implementasikan localStorage atau backend

### Modal tidak muncul
- Pastikan tidak ada error di console
- Cek apakah modal element ada di HTML
- Verify app.js ter-load dengan baik

## 📄 Lisensi

Educational Project - Sistem Manajemen Event Web3

## 👨‍💻 Developer

**Nuril Akmal** (2509106074)
PRAKTIKUM APD B2 - Event Management System

---

**Last Updated**: November 2025
**Version**: 1.0.0
