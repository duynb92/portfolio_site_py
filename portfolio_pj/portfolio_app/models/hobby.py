import uuid
from django.db import models


class Hobby(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    quote = models.TextField()
    author = models.CharField(max_length=200)
    # CSS class name like flaticon-open-book, not a URL
    image = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
