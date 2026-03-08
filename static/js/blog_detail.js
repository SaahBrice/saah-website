/**
 * Blog Detail — Like button + Share (Alpine.js)
 */

function blogDetail(blogId, realLikes, totalLikes) {
    return {
        blogId: blogId,
        realLikes: realLikes,
        totalLikes: totalLikes,
        liked: false,
        copied: false,

        async like() {
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
                    this.liked = true;
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
                // Fallback
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
