/**
 * Blog Detail — Escalating Like Button + Share
 * The more you click, the crazier it gets! 💜
 */

function blogDetail(blogId, realLikes, totalLikes) {
    return {
        blogId: blogId,
        realLikes: realLikes,
        totalLikes: totalLikes,
        liked: false,
        copied: false,
        clickCount: 0,
        animClass: '',
        toastMsg: '',
        toastVisible: false,
        toastTimer: null,

        // Escalating messages
        messages: [
            ['💜 Nice! Tap again!', '👀 One more?', '💜 Don\'t be shy, keep going!'],
            ['🔥 You\'re warming up!', '⚡ Keep smashing it!', '💪 More power!', '🎯 On a roll!'],
            ['🚀 UNSTOPPABLE!', '😱 You\'re insane!', '🌪️ LIKE TORNADO!', '💥 BOOM BOOM!', '🤯 Can\'t stop won\'t stop!'],
            ['👑 LEGENDARY STATUS!', '🏆 LIKE GOD ACTIVATED!', '🦄 MYTHICAL LIKER!', '💎 DIAMOND HANDS!', '🫡 We bow to you!', '🐐 The GOAT has spoken!'],
        ],

        getTier() {
            if (this.clickCount <= 1) return 0;
            if (this.clickCount <= 4) return 1;
            if (this.clickCount <= 9) return 2;
            return 3;
        },

        getAnimClass() {
            return `like-anim-${this.getTier() + 1}`;
        },

        getRandomMessage() {
            const tier = this.getTier();
            const msgs = this.messages[tier];
            return msgs[Math.floor(Math.random() * msgs.length)];
        },

        showToast(msg) {
            this.toastMsg = msg;
            this.toastVisible = true;
            clearTimeout(this.toastTimer);
            this.toastTimer = setTimeout(() => {
                this.toastVisible = false;
            }, this.getTier() >= 3 ? 2000 : 1500);
        },

        spawnParticles(count) {
            const btn = this.$refs.likeBtn;
            if (!btn) return;
            const rect = btn.getBoundingClientRect();
            const emojis = ['💜', '💫', '✨', '⚡', '🔥', '💥', '🚀', '👑', '🦄', '💎'];
            const tier = this.getTier();

            for (let i = 0; i < count; i++) {
                const particle = document.createElement('span');
                particle.className = 'like-particle';
                particle.textContent = emojis[Math.floor(Math.random() * Math.min(3 + tier * 2, emojis.length))];

                // Use viewport-relative fixed positioning
                const centerX = rect.left + rect.width / 2;
                const startY = rect.top;
                const xSpread = (Math.random() - 0.5) * 80;

                particle.style.position = 'fixed';
                particle.style.left = (centerX + xSpread) + 'px';
                particle.style.top = startY + 'px';
                particle.style.fontSize = (1 + tier * 0.3 + Math.random() * 0.4) + 'rem';
                particle.style.zIndex = '9999';

                const yDrift = -60 - Math.random() * 60;
                const xDrift = (Math.random() - 0.5) * 100;

                document.body.appendChild(particle);

                particle.animate([
                    { opacity: 1, transform: 'translateY(0) translateX(0) scale(1) rotate(0deg)' },
                    { opacity: 0, transform: `translateY(${yDrift}px) translateX(${xDrift}px) scale(0.3) rotate(${Math.random() * 360}deg)` },
                ], {
                    duration: 800 + Math.random() * 400,
                    easing: 'cubic-bezier(0.16, 1, 0.3, 1)',
                    fill: 'forwards',
                });

                setTimeout(() => particle.remove(), 1300);
            }
        },

        shakeBottomBar() {
            // Only shake the bottom bar, not the whole page
            const bar = this.$refs.likeBtn?.closest('.fixed');
            if (!bar) return;
            bar.classList.add('bar-shake');
            setTimeout(() => bar.classList.remove('bar-shake'), 400);
        },

        async like() {
            this.clickCount++;
            const tier = this.getTier();

            // Remove previous animation class, re-trigger
            this.animClass = '';
            await this.$nextTick();
            this.animClass = this.getAnimClass();

            // Spawn particles (more with each tier)
            const particleCounts = [1, 3, 6, 12];
            this.spawnParticles(particleCounts[tier]);

            // Shake bottom bar on tier 3+ (not the whole page)
            if (tier >= 3) this.shakeBottomBar();

            // Show toast message
            this.showToast(this.getRandomMessage());

            this.liked = true;

            // API call
            try {
                const res = await fetch(`/api/blogs/${this.blogId}/like/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': this.getCookie('csrftoken'),
                    },
                });
                if (res.ok) {
                    const data = await res.json();
                    this.realLikes = data.real_likes;
                    this.totalLikes = data.total_likes;
                }
            } catch (err) {
                console.error('Like failed:', err);
            }
        },

        async copyLink() {
            try {
                await navigator.clipboard.writeText(window.location.href);
                this.copied = true;
                setTimeout(() => { this.copied = false; }, 2000);
            } catch (err) {
                const ta = document.createElement('textarea');
                ta.value = window.location.href;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
                this.copied = true;
                setTimeout(() => { this.copied = false; }, 2000);
            }
        },

        getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
            return '';
        },
    };
}
