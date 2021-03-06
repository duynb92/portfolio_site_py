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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from portfolio_app.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('portfolio', portfolio),
    path('services', service),
    path('contact', contact),
    path('profile', profile),
    path('blog/<int:blog_year>/<int:blog_month>', blogArchive),
    path('blog/<int:blog_year>/<int:blog_month>/<int:blog_day>/<slug:blog_slug>', blogWithSlug),
    path('blog/tag/<slug:tag_slug>', blogWithTag),
    path('blog/category/<slug:category_slug>', blogWithCategory),
    path('blog', blog),
    path('cv', cv),
    path('', index),
    
] + staticfiles_urlpatterns()
