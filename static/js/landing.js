/**
 * SAAH Landing Page — Countdown + Scroll Reveal
 * Target date: May 8, 2026
 */

function landingApp() {
    return {
        days: '00',
        hours: '00',
        minutes: '00',
        seconds: '00',
        prevSeconds: '00',
        targetDate: new Date('2026-05-08T00:00:00+01:00'),
        interval: null,

        init() {
            this.updateCountdown();
            this.interval = setInterval(() => this.updateCountdown(), 1000);
            this.initScrollReveal();
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

            const newDays = String(d).padStart(2, '0');
            const newHours = String(h).padStart(2, '0');
            const newMinutes = String(m).padStart(2, '0');
            const newSeconds = String(s).padStart(2, '0');

            // Animate only changed values
            if (newDays !== this.days) this.animateDigit('days');
            if (newHours !== this.hours) this.animateDigit('hours');
            if (newMinutes !== this.minutes) this.animateDigit('minutes');
            if (newSeconds !== this.seconds) this.animateDigit('seconds');

            this.days = newDays;
            this.hours = newHours;
            this.minutes = newMinutes;
            this.seconds = newSeconds;
        },

        animateDigit(ref) {
            const el = this.$refs[ref];
            if (!el) return;
            el.style.transform = 'translateY(-4px)';
            el.style.opacity = '0.4';
            requestAnimationFrame(() => {
                setTimeout(() => {
                    el.style.transform = 'translateY(0)';
                    el.style.opacity = '1';
                }, 60);
            });
        },

        initScrollReveal() {
            const elements = document.querySelectorAll('.scroll-reveal');
            if (!elements.length) return;

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.15,
                rootMargin: '0px 0px -40px 0px',
            });

            elements.forEach(el => observer.observe(el));
        },
    };
}
