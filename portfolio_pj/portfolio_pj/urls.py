"""portfolio_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from portfolio_app.sitemaps import StaticSitemap
from portfolio_app.views import *

sitemaps = {
    "static": StaticSitemap,
}

urlpatterns = [
    path('admin', admin.site.urls),
    path('sitemap.xml', sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('services', service, name="service"),
    path('lab', lab, name="lab"),
    path('contact', contact, name="contact"),
    path('profile', profile, name="profile"),
    path('blog/<int:blog_year>/<int:blog_month>', blogArchive, name="blog_archive"),
    path('blog/<int:blog_year>/<int:blog_month>/<int:blog_day>/<slug:blog_slug>', blogWithSlug, name="blog_detail"),
    path('blog/tag/<slug:tag_slug>', blogWithTag, name="blog_tag"),
    path('blog/category/<slug:category_slug>', blogWithCategory, name="blog_category"),
    path('blog', blog, name="blog"),
    path('cv', cv, name="cv"),
    path('', index, name="index"),

] + staticfiles_urlpatterns()
