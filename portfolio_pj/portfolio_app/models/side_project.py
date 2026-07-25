import uuid
import json
from django.db import models


class SideProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)
    tech_tags_raw = models.TextField(default='[]', help_text='JSON list of strings, e.g. ["nextjs", "typescript"]')
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
