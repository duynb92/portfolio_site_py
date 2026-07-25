import uuid
from django.db import models


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    percent = models.CharField(max_length=10)
    icon = models.URLField(max_length=500, blank=True, default="")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
