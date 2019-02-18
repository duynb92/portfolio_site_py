import uuid
from django.db import models
from ckeditor.fields import RichTextField
import re
from autoslug import AutoSlugField

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title',unique=True,null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title',unique=True,null=True)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',unique=True,null=True)
    content = RichTextField()
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def getPreview(self):
        return self.remove_tags(self.content)[:300] + "..."

    def getDateOnly(self):
        return self.pub_date.strftime("%d")

    def getMonthOnly(self):
        return self.pub_date.strftime("%b")

    def getMonth(self):
        return self.pub_date.strftime("%m")

    def getYearOnly(self):
        return self.pub_date.strftime("%Y")

    @staticmethod
    def getArchives():
        blogs = Blog.objects.all().order_by('-pub_date')
        archives = {}
        for blog in blogs:
            if blog.getYearOnly() in archives:
                if blog.getMonth() not in archives[blog.getYearOnly()]:
                    archives[blog.getYearOnly()].append(blog.getMonth())
            else:
                archives[blog.getYearOnly()] = [blog.getMonth()]
        return archives


    def remove_tags(self, text):
        return re.compile(r'<[^>]+>').sub('', text)

