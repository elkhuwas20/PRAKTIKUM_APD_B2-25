// ============ ADVANCED FEATURES & UTILITIES ============

// ============ LOCAL STORAGE MANAGEMENT ============
const StorageManager = {
    saveData() {
        try {
            localStorage.setItem('web3EventsAppData', JSON.stringify(appData));
            console.log('Data saved to localStorage');
        } catch (e) {
            console.error('Error saving to localStorage:', e);
        }
    },

    loadData() {
        try {
            const saved = localStorage.getItem('web3EventsAppData');
            if (saved) {
                const parsedData = JSON.parse(saved);
                // Merge dengan default data
                appData.users = parsedData.users || appData.users;
                appData.events = parsedData.events || appData.events;
                appData.currentUser = parsedData.currentUser || null;
                console.log('Data loaded from localStorage');
            }
        } catch (e) {
            console.error('Error loading from localStorage:', e);
        }
    },

    clearData() {
        localStorage.removeItem('web3EventsAppData');
        console.log('LocalStorage cleared');
    },

    exportData() {
        const dataStr = JSON.stringify(appData, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        const url = URL.createObjectURL(dataBlob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `web3-events-backup-${new Date().getTime()}.json`;
        link.click();
    }
};

// ============ EVENT ANALYTICS ============
const Analytics = {
    getEventStats(eventId) {
        const event = appData.events.find(e => e.id === eventId);
        if (!event) return null;

        return {
            id: event.id,
            name: event.name,
            totalParticipants: event.participants.length,
            status: event.status,
            registrationRate: ((event.participants.length / 100) * 100).toFixed(2) + '%'
        };
    },

    getAllStats() {
        const totalEvents = appData.events.length;
        const totalParticipants = appData.events.reduce((sum, e) => sum + e.participants.length, 0);
        const ongoingEvents = appData.events.filter(e => e.status === 'ongoing').length;
        const finishedEvents = appData.events.filter(e => e.status === 'finished').length;

        return {
            totalEvents,
            totalParticipants,
            ongoingEvents,
            finishedEvents,
            averageParticipantsPerEvent: (totalParticipants / totalEvents).toFixed(1)
        };
    },

    getUserStats(username) {
        const userEvents = appData.events.filter(e => e.participants.includes(username));
        const ongoingRegistrations = userEvents.filter(e => e.status === 'ongoing').length;
        const finishedEvents = userEvents.filter(e => e.status === 'finished').length;

        return {
            username,
            totalEvents: userEvents.length,
            ongoingRegistrations,
            finishedEvents,
            events: userEvents
        };
    }
};

// ============ EVENT SEARCH & FILTER ============
const EventSearch = {
    searchByName(keyword) {
        return appData.events.filter(e => 
            e.name.toLowerCase().includes(keyword.toLowerCase())
        );
    },

    filterByStatus(status) {
        return appData.events.filter(e => e.status === status);
    },

    filterByPrizeRange(minPrize, maxPrize) {
        return appData.events.filter(e => {
            const prizeNum = parseInt(e.prize);
            return prizeNum >= minPrize && prizeNum <= maxPrize;
        });
    },

    sortByParticipants(order = 'desc') {
        const sorted = [...appData.events].sort((a, b) => {
            return order === 'desc' 
                ? b.participants.length - a.participants.length
                : a.participants.length - b.participants.length;
        });
        return sorted;
    },

    advancedSearch(criteria) {
        return appData.events.filter(e => {
            let matches = true;

            if (criteria.keyword) {
                matches &= e.name.toLowerCase().includes(criteria.keyword.toLowerCase());
            }

            if (criteria.status) {
                matches &= e.status === criteria.status;
            }

            if (criteria.minParticipants) {
                matches &= e.participants.length >= criteria.minParticipants;
            }

            if (criteria.maxParticipants) {
                matches &= e.participants.length <= criteria.maxParticipants;
            }

            return matches;
        });
    }
};

// ============ DATA VALIDATION ============
const Validator = {
    isValidUsername(username) {
        return username.length >= 3 && username.length <= 20 && /^[a-zA-Z0-9_]+$/.test(username);
    },

    isValidPassword(password) {
        return password.length >= 6;
    },

    isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    },

    isValidEventName(name) {
        return name.length >= 3 && name.length <= 100;
    },

    validateEvent(event) {
        const errors = [];

        if (!this.isValidEventName(event.name)) {
            errors.push('Event name harus 3-100 karakter');
        }

        if (!event.prize || event.prize.trim() === '') {
            errors.push('Prize tidak boleh kosong');
        }

        if (!['ongoing', 'finished'].includes(event.status)) {
            errors.push('Status harus ongoing atau finished');
        }

        return {
            isValid: errors.length === 0,
            errors
        };
    }
};

// ============ EXPORT/IMPORT FUNCTIONS ============
const DataExchange = {
    exportAsCSV() {
        let csv = 'ID,Event Name,Prize,Status,Participants Count\n';

        appData.events.forEach(event => {
            csv += `${event.id},"${event.name}","${event.prize}",${event.status},${event.participants.length}\n`;
        });

        const blob = new Blob([csv], { type: 'text/csv' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `events-${new Date().getTime()}.csv`;
        link.click();
    },

    exportAsJSON() {
        StorageManager.exportData();
    },

    importFromJSON(jsonString) {
        try {
            const importedData = JSON.parse(jsonString);
            
            if (importedData.events && Array.isArray(importedData.events)) {
                appData.events = importedData.events;
                return { success: true, message: 'Data imported successfully' };
            }
            return { success: false, message: 'Invalid JSON format' };
        } catch (e) {
            return { success: false, message: 'Error parsing JSON: ' + e.message };
        }
    }
};

// ============ EMAIL SIMULATION ============
const EmailService = {
    sendRegistrationEmail(username, email) {
        console.log(`📧 Email sent to ${email}`);
        console.log(`Welcome to Web3 Events, ${username}!`);
        return true;
    },

    sendEventReminderEmail(username, eventName) {
        console.log(`📧 Reminder email sent`);
        console.log(`Reminder: You are registered for ${eventName}`);
        return true;
    },

    sendConfirmationEmail(username, eventName) {
        console.log(`📧 Confirmation email sent`);
        console.log(`You have successfully registered for ${eventName}`);
        return true;
    }
};

// ============ NOTIFICATION SYSTEM ============
const NotificationManager = {
    notifications: [],

    create(message, type = 'info', duration = 3000) {
        const notification = {
            id: Date.now(),
            message,
            type,
            timestamp: new Date()
        };

        this.notifications.push(notification);
        showNotification(message, type);

        if (duration > 0) {
            setTimeout(() => this.remove(notification.id), duration);
        }

        return notification.id;
    },

    remove(id) {
        this.notifications = this.notifications.filter(n => n.id !== id);
    },

    getAll() {
        return this.notifications;
    },

    clearAll() {
        this.notifications = [];
    }
};

// ============ LOGGING SYSTEM ============
const Logger = {
    logs: [],
    maxLogs: 100,

    log(message, level = 'info') {
        const logEntry = {
            timestamp: new Date(),
            level,
            message
        };

        this.logs.push(logEntry);

        if (this.logs.length > this.maxLogs) {
            this.logs.shift();
        }

        console.log(`[${level.toUpperCase()}] ${message}`);
        return logEntry;
    },

    info(message) { return this.log(message, 'info'); },
    warn(message) { return this.log(message, 'warn'); },
    error(message) { return this.log(message, 'error'); },
    debug(message) { return this.log(message, 'debug'); },

    getLogs(level = null) {
        if (level) {
            return this.logs.filter(l => l.level === level);
        }
        return this.logs;
    },

    exportLogs() {
        const logStr = this.logs.map(l => 
            `[${l.timestamp.toISOString()}] [${l.level.toUpperCase()}] ${l.message}`
        ).join('\n');

        const blob = new Blob([logStr], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `logs-${new Date().getTime()}.txt`;
        link.click();
    }
};

// ============ USER ACTIVITY TRACKER ============
const ActivityTracker = {
    activities: [],
    maxActivities: 500,

    trackLogin(username) {
        this.add('LOGIN', username, `User ${username} logged in`);
    },

    trackLogout(username) {
        this.add('LOGOUT', username, `User ${username} logged out`);
    },

    trackEventRegistration(username, eventName) {
        this.add('REGISTER', username, `${username} registered for ${eventName}`);
    },

    trackEventCreation(username, eventName) {
        this.add('CREATE_EVENT', username, `${username} created event ${eventName}`);
    },

    trackEventUpdate(username, eventName) {
        this.add('UPDATE_EVENT', username, `${username} updated event ${eventName}`);
    },

    trackEventDelete(username, eventName) {
        this.add('DELETE_EVENT', username, `${username} deleted event ${eventName}`);
    },

    add(action, username, description) {
        const activity = {
            timestamp: new Date(),
            action,
            username,
            description
        };

        this.activities.push(activity);

        if (this.activities.length > this.maxActivities) {
            this.activities.shift();
        }

        Logger.log(`Activity: ${action} by ${username}`);
    },

    getActivities(username = null) {
        if (username) {
            return this.activities.filter(a => a.username === username);
        }
        return this.activities;
    },

    getActivityReport(username = null) {
        const activities = this.getActivities(username);
        const report = {};

        activities.forEach(activity => {
            report[activity.action] = (report[activity.action] || 0) + 1;
        });

        return report;
    }
};

// ============ PERFORMANCE MONITORING ============
const Performance = {
    metrics: {},

    startMeasure(name) {
        this.metrics[name] = {
            start: performance.now(),
            end: null,
            duration: null
        };
    },

    endMeasure(name) {
        if (this.metrics[name]) {
            this.metrics[name].end = performance.now();
            this.metrics[name].duration = this.metrics[name].end - this.metrics[name].start;
            console.log(`[PERFORMANCE] ${name}: ${this.metrics[name].duration.toFixed(2)}ms`);
            return this.metrics[name];
        }
    },

    getMetrics() {
        return this.metrics;
    }
};

// ============ BACKUP & RESTORE ============
const BackupManager = {
    createBackup(name = null) {
        const backup = {
            name: name || `backup-${new Date().toISOString()}`,
            timestamp: new Date(),
            data: JSON.parse(JSON.stringify(appData))
        };

        localStorage.setItem(`backup_${backup.name}`, JSON.stringify(backup));
        Logger.log(`Backup created: ${backup.name}`);
        return backup;
    },

    getBackups() {
        const backups = [];
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            if (key.startsWith('backup_')) {
                backups.push(JSON.parse(localStorage.getItem(key)));
            }
        }
        return backups;
    },

    restoreBackup(name) {
        const backup = localStorage.getItem(`backup_${name}`);
        if (backup) {
            const backupData = JSON.parse(backup);
            appData.events = backupData.data.events;
            appData.users = backupData.data.users;
            Logger.log(`Backup restored: ${name}`);
            return true;
        }
        Logger.warn(`Backup not found: ${name}`);
        return false;
    },

    deleteBackup(name) {
        localStorage.removeItem(`backup_${name}`);
        Logger.log(`Backup deleted: ${name}`);
    }
};

// ============ AUTOMATIC FEATURES ============
// Auto-save setiap 30 detik
setInterval(() => {
    if (appData.events.length > 0) {
        StorageManager.saveData();
    }
}, 30000);

// Track page visibility
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        ActivityTracker.add('PAGE_HIDDEN', appData.currentUser?.username || 'guest', 'User left the page');
    } else {
        ActivityTracker.add('PAGE_VISIBLE', appData.currentUser?.username || 'guest', 'User returned to page');
    }
});

// Export utilities untuk digunakan di console
window.Utilities = {
    Storage: StorageManager,
    Analytics,
    Search: EventSearch,
    Validator,
    Export: DataExchange,
    Email: EmailService,
    Notifications: NotificationManager,
    Logger,
    Activity: ActivityTracker,
    Perf: Performance,
    Backup: BackupManager
};

console.log('%cWeb3 Events Advanced Features Loaded', 'color: #6366f1; font-size: 14px; font-weight: bold;');
console.log('Available utilities: window.Utilities');
console.log('Example: window.Utilities.Analytics.getAllStats()');
