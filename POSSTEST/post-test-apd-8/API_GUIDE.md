# Web3 Event Manager - API & Developer Guide

Panduan lengkap untuk developer dan advanced users.

## 📚 API Reference

### Event Management API

#### `createEventCard(event, isAdmin)`
Membuat elemen HTML untuk event card.

```javascript
// Usage
const card = createEventCard(event, false);
document.getElementById('eventsGrid').appendChild(card);

// Parameters
- event: Object | Event data
- isAdmin: Boolean | Show admin buttons (optional)
```

#### `registerEvent(eventId)`
Mendaftarkan user ke event.

```javascript
registerEvent(1);  // Register to event with ID 1

// Returns
- void (menampilkan notification)
```

#### `handleCreateEvent(e)`
Handle form submission untuk create event.

```javascript
// Auto dipanggil oleh form submit
// Event harus terisi: name, prize, status
```

#### `openEditModal(eventId)`
Membuka modal untuk edit event.

```javascript
openEditModal(1);  // Open edit modal for event 1
```

#### `handleUpdateEvent(e)`
Update data event.

```javascript
// Auto dipanggil saat form submit
```

#### `handleDeleteEvent(eventId)`
Menghapus event dengan konfirmasi.

```javascript
handleDeleteEvent(1);  // Delete event with ID 1
```

---

### User Authentication API

#### `handleLogin(e)`
Proses login user.

```javascript
// Form submission handler
// Required fields: username, password
// Returns: Sets appData.currentUser
```

#### `handleRegister(e)`
Proses registrasi user baru.

```javascript
// Form submission handler
// Required fields: username, password, confirmPassword
// Password harus minimal 6 karakter
```

#### `handleLogout()`
Logout user saat ini.

```javascript
handleLogout();  // Logout dan redirect ke home
```

---

### Navigation API

#### `navigateTo(page)`
Navigate ke halaman tertentu.

```javascript
navigateTo('home');        // Home page
navigateTo('auth');        // Auth page
navigateTo('events');      // Public events page
navigateTo('dashboard');   // User dashboard
```

#### `switchAuthTab(tab)`
Switch antara login dan register.

```javascript
switchAuthTab('login');     // Tampilkan login form
switchAuthTab('register');  // Tampilkan register form
```

#### `switchDashboardTab(tabName)`
Switch dashboard tabs.

```javascript
switchDashboardTab('dashboard');  // Dashboard tab
switchDashboardTab('events');     // Events tab
switchDashboardTab('create');     // Create event tab
switchDashboardTab('myevents');   // My events tab
```

---

### Render & Display API

#### `renderEvents(containerId)`
Render event cards ke container.

```javascript
renderEvents('eventsGrid');        // Render ke events grid
renderEvents('dashboardEventsGrid'); // Render ke dashboard
```

#### `renderDashboard()`
Render full dashboard dengan all tabs.

```javascript
renderDashboard();  // Update seluruh dashboard
```

#### `renderDashboardStats()`
Update statistics cards.

```javascript
renderDashboardStats();  // Update stat values
```

#### `renderDashboardEvents()`
Update events table di dashboard.

```javascript
renderDashboardEvents();  // Refresh events table
```

#### `renderMyEvents()`
Render events yang user sudah daftar.

```javascript
renderMyEvents();  // Update my events grid
```

---

### Notification API

#### `showNotification(message, type)`
Tampilkan notification toast.

```javascript
showNotification('Success!', 'success');   // Green
showNotification('Error!', 'error');       // Red
showNotification('Warning!', 'warning');   // Yellow
showNotification('Info', 'info');          // Default
```

---

### Advanced Features API

Semua advanced features dapat diakses via `window.Utilities`:

```javascript
window.Utilities.Analytics.getAllStats();
window.Utilities.Search.searchByName('ETH');
window.Utilities.Logger.log('Message');
// dll
```

#### Storage Manager
```javascript
// Save data to localStorage
Utilities.Storage.saveData();

// Load data from localStorage
Utilities.Storage.loadData();

// Clear localStorage
Utilities.Storage.clearData();

// Export data as JSON
Utilities.Storage.exportData();
```

#### Analytics
```javascript
// Get stats untuk semua events
Utilities.Analytics.getAllStats();
// Returns: { totalEvents, totalParticipants, ongoingEvents, finishedEvents, ... }

// Get stats untuk specific event
Utilities.Analytics.getEventStats(1);

// Get stats untuk specific user
Utilities.Analytics.getUserStats('Bang Pernanda');
```

#### Event Search & Filter
```javascript
// Search by name
Utilities.Search.searchByName('Hackathon');

// Filter by status
Utilities.Search.filterByStatus('ongoing');

// Sort by participants
Utilities.Search.sortByParticipants('desc');  // desc or asc

// Advanced search
Utilities.Search.advancedSearch({
    keyword: 'ETH',
    status: 'ongoing',
    minParticipants: 0,
    maxParticipants: 100
});
```

#### Data Validation
```javascript
// Validate username
Utilities.Validator.isValidUsername('newUser');  // true/false

// Validate password
Utilities.Validator.isValidPassword('password123');  // true/false

// Validate event
Utilities.Validator.validateEvent(eventObject);
// Returns: { isValid: true/false, errors: [...] }
```

#### Data Exchange
```javascript
// Export as CSV
Utilities.Export.exportAsCSV();

// Export as JSON
Utilities.Export.exportAsJSON();

// Import from JSON string
Utilities.Export.importFromJSON(jsonString);
```

#### Logger
```javascript
// Log messages
Utilities.Logger.log('Message', 'info');
Utilities.Logger.info('Info message');
Utilities.Logger.warn('Warning message');
Utilities.Logger.error('Error message');
Utilities.Logger.debug('Debug message');

// Get all logs
Utilities.Logger.getLogs();

// Get logs by level
Utilities.Logger.getLogs('error');

// Export logs
Utilities.Logger.exportLogs();
```

#### Activity Tracking
```javascript
// Track activities
Utilities.Activity.trackLogin('username');
Utilities.Activity.trackEventRegistration('username', 'Event Name');
Utilities.Activity.trackEventCreation('username', 'Event Name');

// Get activities
Utilities.Activity.getActivities();  // All activities
Utilities.Activity.getActivities('username');  // User activities

// Get activity report
Utilities.Activity.getActivityReport();
```

#### Backup & Restore
```javascript
// Create backup
Utilities.Backup.createBackup('my-backup');

// Get all backups
Utilities.Backup.getBackups();

// Restore backup
Utilities.Backup.restoreBackup('my-backup');

// Delete backup
Utilities.Backup.deleteBackup('my-backup');
```

---

## 🔧 Customization Guide

### 1. Mengubah Default Events

Edit di `app.js`, bagian `appData.events`:

```javascript
const appData = {
    events: [
        {
            id: 1,
            name: "Event Name",
            prize: "10.000 USDT",
            status: "ongoing",  // ongoing atau finished
            participants: [],
            description: "Event description"
        }
    ]
};
```

### 2. Mengubah Default Users

Edit di `app.js`, bagian `appData.users`:

```javascript
appData.users = [
    { username: "user1", password: "pass123", type: "user" },
    { username: "admin1", password: "admin123", type: "admin" }
];
```

### 3. Mengubah Tema Warna

Edit di `styles.css`, bagian `:root`:

```css
:root {
    --primary-color: #6366f1;      /* Ubah ke warna pilihan */
    --secondary-color: #8b5cf6;
    --tertiary-color: #ec4899;
    --dark-bg: #0f172a;
    /* dll */
}
```

### 4. Menambah Menu Item

Di `index.html`, tambah ke navbar:

```html
<a href="#" class="nav-link" data-page="new-page">New Page</a>
```

Di `app.js`, tambah handler:

```javascript
} else if (page === 'new-page') {
    document.getElementById('newPage').style.display = 'block';
}
```

### 5. Menambah Form Field

Di `index.html`, tambah input:

```html
<div class="form-group">
    <label for="fieldName">Field Label</label>
    <input type="text" id="fieldName" required>
</div>
```

Di `app.js`, akses value:

```javascript
const value = document.getElementById('fieldName').value;
```

---

## 🔌 Integration Guide

### 1. Backend Integration (Node.js)

```javascript
// Di app.js, ganti handleLogin:
async function handleLogin(e) {
    e.preventDefault();
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        if (data.success) {
            appData.currentUser = data.user;
            showNotification('Login berhasil!', 'success');
            navigateTo('dashboard');
        } else {
            showNotification('Login gagal', 'error');
        }
    } catch (error) {
        showNotification('Error: ' + error.message, 'error');
    }
}
```

### 2. Database Integration

```javascript
// Fetch events dari API
async function loadEvents() {
    try {
        const response = await fetch('/api/events');
        const events = await response.json();
        appData.events = events;
        renderEvents('eventsGrid');
    } catch (error) {
        console.error('Error loading events:', error);
    }
}

// Create event ke API
async function createEventAPI(eventData) {
    try {
        const response = await fetch('/api/events', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(eventData)
        });
        const newEvent = await response.json();
        appData.events.push(newEvent);
        showNotification('Event created!', 'success');
    } catch (error) {
        showNotification('Error: ' + error.message, 'error');
    }
}
```

### 3. LocalStorage Persistence

Tambah ke `app.js`:

```javascript
// Save sebelum logout
function handleLogout() {
    if (confirm('Yakin ingin logout?')) {
        StorageManager.saveData();  // Save first
        appData.currentUser = null;
        showNotification('Anda telah logout', 'success');
        navigateTo('home');
    }
}

// Load on page start
document.addEventListener('DOMContentLoaded', () => {
    StorageManager.loadData();  // Load before everything
    navigateTo('home');
});
```

---

## 📊 Data Models

### Event Object
```javascript
{
    id: Number,                    // Unique ID
    name: String,                  // Event name
    prize: String,                 // Prize pool
    status: String,                // 'ongoing' | 'finished'
    participants: Array<String>,   // List of usernames
    description: String            // Event description
}
```

### User Object
```javascript
{
    username: String,              // Unique username
    password: String,              // Password (hash in production)
    type: String                   // 'user' | 'admin'
}
```

### CurrentUser Object
```javascript
{
    username: String,
    type: String                   // 'user' | 'admin'
}
```

---

## 🧪 Testing Examples

### Test di Console Browser

```javascript
// Test analytics
console.log(Utilities.Analytics.getAllStats());

// Test search
console.log(Utilities.Search.searchByName('Hackathon'));

// Test validation
console.log(Utilities.Validator.isValidUsername('user123'));

// Test backup
Utilities.Backup.createBackup('test');
console.log(Utilities.Backup.getBackups());

// Test activity
console.log(Utilities.Activity.getActivityReport());
```

---

## 🐛 Debugging Tips

### Enable Detailed Logging

```javascript
// Di advanced-features.js
const DEBUG_MODE = true;

if (DEBUG_MODE) {
    // Additional logging
}
```

### Check Data Structure

```javascript
// Di console
console.log(appData);
console.log(appData.events);
console.log(appData.currentUser);
```

### Monitor Performance

```javascript
// Di console
Utilities.Perf.startMeasure('renderEvents');
renderEvents('eventsGrid');
Utilities.Perf.endMeasure('renderEvents');
```

---

## 📋 Version History

### v1.0.0 (Current)
- Initial release
- Auth system
- Event management
- Dashboard
- Advanced features

### v1.1.0 (Planned)
- Backend integration
- Real database
- User profile
- Event reviews
- Payment system

---

## 📞 Support

Untuk pertanyaan atau issues, silakan buat issue di repository.

**Developer**: Nuril Akmal (2509106074)
