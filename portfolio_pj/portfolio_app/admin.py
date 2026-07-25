from django.contrib import admin
from .models import (
    Blog, Tag, Category, BlogComment,
    Skill, Certification, Hobby, Service, SideProject,
    Profile, ProfileItem, Project, Link,
)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'order')
    list_editable = ('order',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'order')
    list_editable = ('order',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(SideProject)
class SideProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail', 'order')
    list_editable = ('order',)


class ProfileItemInline(admin.StackedInline):
    model = ProfileItem
    extra = 0
    fields = ('time', 'title', 'sub_title', 'descriptions_raw', 'link', 'is_active', 'order')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('header', 'order')
    list_editable = ('order',)
    inlines = [ProfileItemInline]


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0
    fields = ('url', 'platform')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag', 'client', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    inlines = [LinkInline]
