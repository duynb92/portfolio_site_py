import uuid
import json
from django.db import models


class ProjectCategory:
    MOBILE = 1
    WEB = 2
    DESKTOP = 3
    LINUX = 4


class ProjectPlatform:
    IOS = 1
    ANDROID = 2
    WEB = 3
    WINDOWS = 4


# Aliases for backward compatibility
Category = ProjectCategory
Platform = ProjectPlatform


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    tag = models.CharField(max_length=100)
    filters = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200)
    roles = models.CharField(max_length=200)
    skills = models.CharField(max_length=500)
    length = models.CharField(max_length=100)
    # JSON list of ints matching ProjectCategory constants
    categories_raw = models.TextField(default='[]')
    screenshots = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    @property
    def categories(self):
        return json.loads(self.categories_raw)

    @property
    def links(self):
        return self.link_set.all()


class Link(models.Model):
    PLATFORM_CHOICES = [
        (ProjectPlatform.IOS, 'iOS'),
        (ProjectPlatform.ANDROID, 'Android'),
        (ProjectPlatform.WEB, 'Web'),
        (ProjectPlatform.WINDOWS, 'Windows'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
    platform = models.PositiveSmallIntegerField(choices=PLATFORM_CHOICES)

    def __str__(self):
        return self.url
