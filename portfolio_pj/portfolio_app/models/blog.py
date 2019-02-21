import uuid
from django.db import models
from ckeditor.fields import RichTextField
import re
from autoslug import AutoSlugField
from pytz import timezone, utc
from django.conf import settings
# from django.utils import timezone

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

    def getDateTime(self):
        return self.pub_date.strftime("%d, %B, %Y")

    def getDateOnly(self):
        return self.pub_date.strftime("%d")

    def getMonthOnly(self):
        return self.pub_date.strftime("%b")

    def getMonth(self):
        return self.pub_date.strftime("%m")

    def getYearOnly(self):
        return self.pub_date.strftime("%Y")

    def getFirstImageUrl(self):
        start = self.content.find("<img")
        if (start > -1):
            end = self.content.find("</img>")
            substring = self.content[start:end]
            return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', substring)[0]
        else:
            return None

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

class BlogComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField(max_length=1000)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def isParent(self):
        if self.parent is None:
            return True
        else:
            return False

    def utcisoformat(self):
    # Return a datetime object in ISO 8601 format in UTC, without microseconds
    # or time zone offset other than 'Z', e.g. '2011-06-28T00:00:00Z'. Useful
    # for making Django DateTimeField values compatible with the
    # jquery.localtime plugin.
    # Convert datetime to UTC, remove microseconds, remove timezone, convert to string
        TZ = timezone(settings.TIME_ZONE)
        return TZ.localize(django.utils.timezone.make_aware(self.timestamp).replace(microsecond=0)).astimezone(utc).replace(tzinfo=None).isoformat() + 'Z'