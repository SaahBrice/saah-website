/**
 * SAAH Landing Page — Countdown Timer
 * Target date: May 8, 2026 (2 months from March 8, 2026)
 */

function landingApp() {
    return {
        days: '00',
        hours: '00',
        minutes: '00',
        seconds: '00',
        targetDate: new Date('2026-05-08T00:00:00+01:00'),
        interval: null,

        init() {
            this.updateCountdown();
            this.interval = setInterval(() => this.updateCountdown(), 1000);
        },

        updateCountdown() {
            const now = new Date();
            const diff = this.targetDate - now;

            if (diff <= 0) {
                this.days = '00';
                this.hours = '00';
                this.minutes = '00';
                this.seconds = '00';
                clearInterval(this.interval);
                return;
            }

            const d = Math.floor(diff / (1000 * 60 * 60 * 24));
            const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const s = Math.floor((diff % (1000 * 60)) / 1000);

            this.days = String(d).padStart(2, '0');
            this.hours = String(h).padStart(2, '0');
            this.minutes = String(m).padStart(2, '0');
            this.seconds = String(s).padStart(2, '0');
        },
    };
}
