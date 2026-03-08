"""
Management command to create realistic dummy blog posts for SAAH.
Usage:  python manage.py seed_blogs
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Blog


POSTS = [
    {
        "title": "Why Every Serious Student Needs a Dedicated Workspace",
        "subtitle": "The science behind environment and productivity — and how SAAH is designed around it.",
        "content": """
<p>We've all been there — trying to study at home while distractions pile up. The TV is on, someone's cooking, your phone keeps buzzing. Research shows that environment plays a <strong>critical role</strong> in cognitive performance.</p>

<h2>The Problem with "Studying Anywhere"</h2>
<p>A 2023 study from the University of Cambridge found that students who use dedicated workspaces score <strong>23% higher</strong> on retention tests compared to those who study in shared or multi-purpose spaces.</p>

<blockquote>
"Your brain associates physical spaces with specific activities. When you study in the same place you relax, your brain gets confused signals." — Dr. Amara Nwosu, Cognitive Psychologist
</blockquote>

<h2>What Makes SAAH Different</h2>
<p>At SAAH, every detail is intentional:</p>
<ul>
    <li><strong>Noise-controlled zones</strong> — from silent deep-work areas to collaborative spaces</li>
    <li><strong>Ergonomic furniture</strong> — designed for hours of comfortable focus</li>
    <li><strong>Natural lighting</strong> — studies show it improves alertness by up to 18%</li>
    <li><strong>Fast, reliable Wi-Fi</strong> — because buffering kills momentum</li>
</ul>

<h2>Reserve Your Spot</h2>
<p>SAAH is coming to Buea soon. Be among the first to experience a workspace designed for people who take their work seriously.</p>
""",
        "thumbnail_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=800",
        "audio_url": "",
    },
    {
        "title": "Buea's Growing Tech Scene Needs Better Workspaces",
        "subtitle": "As Silicon Mountain rises, the demand for professional environments is higher than ever.",
        "content": """
<p>Buea has earned its nickname — <strong>Silicon Mountain</strong>. With over 200 startups, a thriving developer community, and growing international attention, the city is becoming one of Central Africa's most exciting tech hubs.</p>

<h2>The Gap We See</h2>
<p>But there's a gap. Despite the talent and ambition, many founders, developers, and remote workers struggle to find spaces that match their drive. Coffee shops close early. Libraries are overcrowded. Home offices are full of interruptions.</p>

<p>A recent survey of 150 Buea-based remote workers revealed:</p>
<ul>
    <li><strong>68%</strong> said finding a quiet workspace is their biggest daily challenge</li>
    <li><strong>74%</strong> would pay for a dedicated, professional environment</li>
    <li><strong>91%</strong> believe a better workspace would directly improve their output</li>
</ul>

<h2>SAAH: Built for Buea</h2>
<p>We're not importing a foreign co-working model. SAAH is built from the ground up for the way Buea works — flexible hours, affordable pricing, and a community-first approach.</p>

<h3>What to Expect</h3>
<p>Think of it as your second home, but purpose-built for getting things done. We're launching with seat reservations, quiet zones, power backup, and lightning-fast internet.</p>
""",
        "thumbnail_url": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800",
        "audio_url": "",
    },
    {
        "title": "The Art of Deep Work: A Guide for Students",
        "subtitle": "Cal Newport's deep work philosophy, adapted for university life in Cameroon.",
        "content": """
<p>In his bestselling book <em>Deep Work</em>, Cal Newport argues that the ability to perform focused, distraction-free work is becoming <strong>one of the most valuable skills</strong> in our economy. But how do you actually practice deep work as a student?</p>

<h2>Rule #1: Time Blocking</h2>
<p>Instead of vaguely planning to "study later," block specific 90-minute windows for deep work. Your brain performs best in 90-minute cycles aligned with your ultradian rhythm.</p>

<h2>Rule #2: Eliminate Digital Noise</h2>
<p>Put your phone on airplane mode. Close social media tabs. Use website blockers if you have to. Studies show it takes an average of <strong>23 minutes</strong> to refocus after a distraction.</p>

<h2>Rule #3: Choose Your Environment</h2>
<p>This is where most students fail. You can't do deep work in a noisy cafeteria or a crowded dorm room. You need a space that signals to your brain: <em>"It's time to focus."</em></p>

<h2>Rule #4: Track Your Output</h2>
<p>Keep a simple log of your deep work hours. Research shows that the mere act of tracking makes you 40% more likely to maintain the habit.</p>

<blockquote>
"Deep work is not about working more hours. It's about making the hours you work actually count."
</blockquote>

<h2>Where SAAH Fits In</h2>
<p>We designed SAAH specifically to support deep work. No distractions. No interruptions. Just you and your most important work.</p>
""",
        "thumbnail_url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800",
        "audio_url": "",
    },
]


class Command(BaseCommand):
    help = "Create realistic dummy blog posts for development."

    def handle(self, *args, **options):
        if Blog.objects.exists():
            self.stdout.write(self.style.WARNING("Blog posts already exist. Skipping."))
            return

        now = timezone.now()
        for i, post_data in enumerate(POSTS):
            Blog.objects.create(
                title=post_data["title"],
                subtitle=post_data["subtitle"],
                content=post_data["content"].strip(),
                thumbnail_url=post_data["thumbnail_url"],
                audio_url=post_data["audio_url"],
                publish_date=now - timezone.timedelta(days=(len(POSTS) - i) * 3),
                edit_date=now - timezone.timedelta(days=(len(POSTS) - i) * 3),
            )
            self.stdout.write(self.style.SUCCESS(f"  ✓ Created: {post_data['title']}"))

        self.stdout.write(self.style.SUCCESS(f"\nDone! Created {len(POSTS)} blog posts."))
