import uuid
from django.db import models


class Certification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    # CharField instead of URLField: some icons are relative paths like img/cert-icons/itil.png
    icon = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
