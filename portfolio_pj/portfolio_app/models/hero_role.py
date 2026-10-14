import uuid
from django.db import models


class HeroRole(models.Model):
    """A line typed out under the name in the home page hero; lines cycle in order."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text
