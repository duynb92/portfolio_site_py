import uuid
import json
from urllib.parse import urlparse
from django.db import models


class SideProject(models.Model):
    STATUS_LIVE = 'live'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_ARCHIVED = 'archived'
    STATUS_CHOICES = (
        (STATUS_LIVE, 'Live'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_ARCHIVED, 'Archived'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    # Blank shows a "Screenshot pending" placeholder on the Lab page
    thumbnail = models.CharField(max_length=200, blank=True)
    tech_tags_raw = models.TextField(default='[]', help_text='JSON list of strings, e.g. ["nextjs", "typescript"]')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_LIVE)
    started = models.DateField(null=True, blank=True, help_text='Shown as month and year, e.g. Mar 2026')
    question = models.TextField(blank=True, help_text='The question the experiment set out to answer')
    result = models.TextField(blank=True, help_text='What came of it')
    notes_raw = models.TextField(default='[]', blank=True, help_text='JSON list of strings shown under "Lab notes"')
    github_url = models.URLField(max_length=500, blank=True, default="")
    demo_url = models.URLField(max_length=500, blank=True, default="")
    apple_store_url = models.URLField(max_length=500, blank=True, default="")
    google_play_url = models.URLField(max_length=500, blank=True, default="")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    @property
    def tech_tags(self):
        return json.loads(self.tech_tags_raw)

    @property
    def notes(self):
        return json.loads(self.notes_raw or '[]')

    @property
    def is_live(self):
        return self.status == self.STATUS_LIVE

    @property
    def is_mobile(self):
        # Store links mean a phone screenshot, which gets a phone frame
        return bool(self.apple_store_url or self.google_play_url)

    @property
    def demo_domain(self):
        return urlparse(self.demo_url).netloc
