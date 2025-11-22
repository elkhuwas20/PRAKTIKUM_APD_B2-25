// ============ DATA STORAGE ============
const appData = {
    users: [
        { username: "Bang Pernanda", password: "123", type: "user" },
        { username: "Mba Triya", password: "321", type: "user" },
        { username: "Nuril Akmal", password: "123", type: "admin" },
        { username: "Akmal Ganteng", password: "321", type: "admin" }
    ],
    events: [
        {
            id: 1,
            name: "ETH Hackathon Samarinda",
            prize: "10.000 USDT + NFT",
            status: "ongoing",
            participants: ["Team Alpha", "Team Beta"],
            description: "Hackathon terbesar untuk developer Ethereum di Samarinda"
        },
        {
            id: 2,
            name: "Solana DeFi Camp",
            prize: "5.000 USDT",
            status: "finished",
            participants: ["DeFi Ninjas"],
            description: "Program pelatihan intensif DeFi di blockchain Solana"
        }
    ],
    currentUser: null
};

let currentEditingEventId = null;

// ============ PAGE NAVIGATION ============
function navigateTo(page) {
    // Hide all pages
    document.getElementById('heroSection').style.display = 'none';
    document.getElementById('authPage').style.display = 'none';
    document.getElementById('eventsPage').style.display = 'none';
    document.getElementById('dashboardPage').style.display = 'none';

    // Update nav menu active state
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
    });

    // Show selected page
    if (page === 'home') {
        document.getElementById('heroSection').style.display = 'block';
        document.querySelector('[data-page="home"]').classList.add('active');
    } else if (page === 'auth') {
        document.getElementById('authPage').style.display = 'block';
        document.querySelector('[data-page="auth"]').classList.add('active');
    } else if (page === 'events') {
        document.getElementById('eventsPage').style.display = 'block';
        document.querySelector('[data-page="events"]').classList.add('active');
        renderEvents('eventsGrid');
    } else if (page === 'dashboard') {
        if (!appData.currentUser) {
            showNotification('Silakan login terlebih dahulu', 'warning');
            navigateTo('auth');
            return;
        }
        document.getElementById('dashboardPage').style.display = 'block';
        renderDashboard();
    }

    window.scrollTo(0, 0);
}

// ============ AUTHENTICATION ============
function switchAuthTab(tab) {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const loginTab = document.getElementById('loginTab');
    const registerTab = document.getElementById('registerTab');

    if (tab === 'login') {
        loginForm.classList.add('active');
        registerForm.classList.remove('active');
        loginTab.classList.add('active');
        registerTab.classList.remove('active');
    } else {
        registerForm.classList.add('active');
        loginForm.classList.remove('active');
        registerTab.classList.add('active');
        loginTab.classList.remove('active');
    }
}

function handleLogin(e) {
    e.preventDefault();
    
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    const user = appData.users.find(u => u.username === username && u.password === password);

    if (user) {
        appData.currentUser = {
            username: user.username,
            type: user.type
        };
        showNotification(`Selamat datang, ${user.username}!`, 'success');
        document.getElementById('loginUsername').value = '';
        document.getElementById('loginPassword').value = '';
        setTimeout(() => navigateTo('dashboard'), 500);
    } else {
        showNotification('Username atau password salah', 'error');
    }
}

function handleRegister(e) {
    e.preventDefault();

    const username = document.getElementById('registerUsername').value;
    const password = document.getElementById('registerPassword').value;
    const confirmPassword = document.getElementById('registerConfirmPassword').value;

    if (password !== confirmPassword) {
        showNotification('Password tidak cocok', 'error');
        return;
    }

    if (password.length < 6) {
        showNotification('Password minimal 6 karakter', 'error');
        return;
    }

    if (appData.users.find(u => u.username === username)) {
        showNotification('Username sudah terdaftar', 'error');
        return;
    }

    appData.users.push({
        username: username,
        password: password,
        type: "user"
    });

    showNotification('Registrasi berhasil! Silakan login', 'success');
    document.getElementById('registerUsername').value = '';
    document.getElementById('registerPassword').value = '';
    document.getElementById('registerConfirmPassword').value = '';
    switchAuthTab('login');
}

function handleLogout() {
    if (confirm('Yakin ingin logout?')) {
        appData.currentUser = null;
        showNotification('Anda telah logout', 'success');
        navigateTo('home');
    }
}

// ============ EVENT MANAGEMENT ============
function renderEvents(containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';

    appData.events.forEach(event => {
        const eventCard = createEventCard(event, false);
        container.appendChild(eventCard);
    });
}

function createEventCard(event, isAdmin = false) {
    const card = document.createElement('div');
    card.className = 'event-card';
    card.innerHTML = `
        <div class="event-header">
            <span class="event-status ${event.status}">${event.status.toUpperCase()}</span>
            <h3 class="event-name">${event.name}</h3>
            <p class="event-description">${event.description || 'Event Web3 terbaik'}</p>
        </div>
        <div class="event-body">
            <div class="event-info">
                <i class="fas fa-trophy"></i>
                <span class="event-prize">${event.prize}</span>
            </div>
            <div class="event-info">
                <i class="fas fa-users"></i>
                <span class="event-participants">${event.participants.length} peserta</span>
            </div>
            <div class="event-actions">
                ${!appData.currentUser ? `<button class="btn btn-secondary btn-sm" onclick="navigateTo('auth')">Login untuk daftar</button>` : 
                  appData.currentUser.type === 'admin' ? `
                    <button class="btn btn-primary btn-sm" onclick="openEditModal(${event.id})">Edit</button>
                    <button class="btn btn-danger btn-sm" onclick="handleDeleteEvent(${event.id})">Delete</button>
                  ` : `
                    <button class="btn btn-primary btn-sm" onclick="registerEvent(${event.id})">Daftar</button>
                  `}
            </div>
        </div>
    `;
    return card;
}

function registerEvent(eventId) {
    if (!appData.currentUser) {
        showNotification('Silakan login terlebih dahulu', 'error');
        return;
    }

    const event = appData.events.find(e => e.id === eventId);
    if (event) {
        if (event.participants.includes(appData.currentUser.username)) {
            showNotification('Anda sudah terdaftar di event ini', 'warning');
        } else if (event.status === 'finished') {
            showNotification('Event ini sudah selesai', 'error');
        } else {
            event.participants.push(appData.currentUser.username);
            showNotification('Berhasil mendaftar event!', 'success');
            renderDashboard();
        }
    }
}

function handleCreateEvent(e) {
    e.preventDefault();

    const name = document.getElementById('eventName').value;
    const prize = document.getElementById('eventPrize').value;
    const status = document.getElementById('eventStatus').value;
    const description = document.getElementById('eventDescription').value;

    if (!name || !prize || !status) {
        showNotification('Semua field wajib diisi', 'error');
        return;
    }

    const newEvent = {
        id: Math.max(...appData.events.map(e => e.id), 0) + 1,
        name: name,
        prize: prize,
        status: status,
        description: description || '',
        participants: []
    };

    appData.events.push(newEvent);
    showNotification('Event berhasil dibuat!', 'success');
    
    document.getElementById('eventName').value = '';
    document.getElementById('eventPrize').value = '';
    document.getElementById('eventStatus').value = '';
    document.getElementById('eventDescription').value = '';

    renderDashboard();
    switchDashboardTab('events');
}

function openEditModal(eventId) {
    const event = appData.events.find(e => e.id === eventId);
    if (event) {
        currentEditingEventId = eventId;
        document.getElementById('modalEventName').value = event.name;
        document.getElementById('modalEventPrize').value = event.prize;
        document.getElementById('modalEventStatus').value = event.status;
        document.getElementById('eventModal').classList.add('active');
    }
}

function closeEventModal() {
    document.getElementById('eventModal').classList.remove('active');
    currentEditingEventId = null;
}

function handleUpdateEvent(e) {
    e.preventDefault();

    if (!currentEditingEventId) return;

    const event = appData.events.find(e => e.id === currentEditingEventId);
    if (event) {
        event.name = document.getElementById('modalEventName').value;
        event.prize = document.getElementById('modalEventPrize').value;
        event.status = document.getElementById('modalEventStatus').value;

        showNotification('Event berhasil diperbarui!', 'success');
        closeEventModal();
        renderDashboard();
    }
}

function handleDeleteEvent(eventId) {
    if (confirm('Yakin ingin menghapus event ini?')) {
        const index = appData.events.findIndex(e => e.id === eventId);
        if (index > -1) {
            appData.events.splice(index, 1);
            showNotification('Event berhasil dihapus!', 'success');
            closeEventModal();
            renderDashboard();
        }
    }
}

// ============ DASHBOARD ============
function renderDashboard() {
    if (!appData.currentUser) return;

    // Update user info
    document.getElementById('userName').textContent = appData.currentUser.username;
    document.getElementById('userRole').textContent = appData.currentUser.type === 'admin' ? 'Administrator' : 'Pengguna';

    // Show/hide admin menu
    const createEventMenu = document.getElementById('createEventMenu');
    if (appData.currentUser.type === 'admin') {
        createEventMenu.style.display = 'block';
    } else {
        createEventMenu.style.display = 'none';
    }

    // Render dashboard tab
    renderDashboardStats();
    renderDashboardEvents();

    // Render events tab
    renderEvents('dashboardEventsGrid');

    // Render my events tab
    renderMyEvents();
}

function renderDashboardStats() {
    const totalEvents = appData.events.length;
    const registeredEvents = appData.events.filter(e => 
        e.participants.includes(appData.currentUser.username)
    ).length;

    document.getElementById('statTotalEvents').textContent = totalEvents;
    document.getElementById('statRegistered').textContent = registeredEvents;
}

function renderDashboardEvents() {
    const container = document.getElementById('dashboardEventsTable');
    container.innerHTML = '';

    if (appData.events.length === 0) {
        container.innerHTML = '<p style="padding: 2rem; text-align: center; color: var(--text-muted);">Belum ada event</p>';
        return;
    }

    const table = document.createElement('div');
    table.innerHTML = `
        <div class="table-header">
            <div>Event Name</div>
            <div>Prize</div>
            <div>Status</div>
            <div>Participants</div>
            <div>Action</div>
        </div>
    `;

    appData.events.forEach(event => {
        const row = document.createElement('div');
        row.className = 'table-row';
        row.innerHTML = `
            <div>${event.name}</div>
            <div>${event.prize}</div>
            <div><span class="event-status ${event.status}">${event.status}</span></div>
            <div>${event.participants.length}</div>
            <div>
                ${appData.currentUser.type === 'admin' ? 
                    `<button class="btn btn-primary btn-sm" onclick="openEditModal(${event.id})">Edit</button>` :
                    !event.participants.includes(appData.currentUser.username) && event.status === 'ongoing' ?
                    `<button class="btn btn-primary btn-sm" onclick="registerEvent(${event.id})">Join</button>` :
                    '<span style="color: var(--success-color);">✓ Joined</span>'
                }
            </div>
        `;
        table.appendChild(row);
    });

    container.appendChild(table);
}

function renderMyEvents() {
    const container = document.getElementById('myEventsGrid');
    container.innerHTML = '';

    const myEvents = appData.events.filter(e => 
        e.participants.includes(appData.currentUser.username)
    );

    if (myEvents.length === 0) {
        container.innerHTML = '<p style="grid-column: 1/-1; text-align: center; padding: 2rem; color: var(--text-muted);">Anda belum mendaftar event apapun</p>';
        return;
    }

    myEvents.forEach(event => {
        const card = createEventCard(event, false);
        container.appendChild(card);
    });
}

function switchDashboardTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });

    // Update menu active state
    document.querySelectorAll('.menu-item').forEach(item => {
        item.classList.remove('active');
    });

    // Show selected tab
    const tabMap = {
        'dashboard': 'dashboardTab',
        'events': 'eventsTab',
        'create': 'createTab',
        'myevents': 'myEventsTab'
    };

    if (tabMap[tabName]) {
        document.getElementById(tabMap[tabName]).classList.add('active');
        event.target?.classList.add('active');
    }
}

// ============ NOTIFICATIONS ============
function showNotification(message, type = 'success') {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type} show`;

    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// ============ MOBILE MENU ============
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
        });
    }

    // Setup nav links
    document.querySelectorAll('[data-page]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const page = link.getAttribute('data-page');
            navigateTo(page);
            if (navMenu.style.display === 'flex') {
                navMenu.style.display = 'none';
            }
        });
    });

    // Initialize with home page
    navigateTo('home');
});

// ============ UTILITY FUNCTIONS ============
function formatCurrency(amount) {
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR'
    }).format(amount);
}

// Close modal when clicking outside
document.addEventListener('click', (e) => {
    const modal = document.getElementById('eventModal');
    if (e.target === modal) {
        closeEventModal();
    }
});

// Add keyboard shortcut for Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeEventModal();
    }
});
