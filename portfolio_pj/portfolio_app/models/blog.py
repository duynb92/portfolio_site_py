from django.db import models
from ckeditor.fields import RichTextField
import re

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    pub_date = models.DateTimeField('date published')

    def getPreview(self):
        return self.remove_tags(self.content)[:200] + "..."

    def getDateOnly(self):
        return self.pub_date.strftime("%d")

    def getMonthOnly(self):
        return self.pub_date.strftime("%b")

    def remove_tags(self, text):
        return re.compile(r'<[^>]+>').sub('', text)

    

    