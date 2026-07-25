import uuid
import json
from django.db import models


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    header = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.header

    @property
    def profileItems(self):
        # Use Prefetch(to_attr='active_items') cache when available (set by Facade),
        # otherwise fall back to a filtered query.
        if hasattr(self, 'active_items'):
            return self.active_items
        return list(self.items.filter(is_active=True))


class ProfileItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='items')
    time = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    sub_title = models.CharField(max_length=200, blank=True, default="")
    descriptions_raw = models.TextField(default='[]', help_text='JSON list of strings, e.g. ["Line 1", "Line 2"]')
    link = models.URLField(max_length=500, blank=True, default="")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    @property
    def subTitle(self):
        return self.sub_title

    @property
    def descriptions(self):
        return json.loads(self.descriptions_raw)
