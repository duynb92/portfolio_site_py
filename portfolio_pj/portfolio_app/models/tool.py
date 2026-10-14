import uuid
from django.db import models


class Tool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    # CharField instead of URLField: icons can be relative static paths like img/icons/x.svg
    icon = models.CharField(max_length=500)
    link = models.URLField(max_length=500, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
