# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.template import RequestContext
import logging
from .models import *
from .forms import *

import os
from django.http import HttpResponse
from portfolio_pj import settings

# Create your views here.
def index(req):
    context = HomeContext("Home", Facade.getSkills(), Facade.getHobbies())
    return render(req, 'index.html', {"context": context})

def profile(req):
    profile_context = ProfileContext("Profile", Facade.getProfiles())
    return render(req, 'profile.html', {"context": profile_context})

def portfolio(req):
    portfolio_context = PortfolioContext("Portfolio", Facade.getProjects())
    return render(req, 'portfolio-gird-3.html', {"context": portfolio_context})

def service(req):
    service_context = ServiceContext("Services", Facade.getServices())
    return render(req, 'services.html', {"context": service_context,})

def contact(req):
    context = BaseContext("Contact")
    return render(req, 'contact-3.html', {"context": context,})

def blog(req):
    print('HERERERE111111')
    blogs = getBlogsWithPaging(req, Blog.objects.all().order_by('-pub_date'))
    blog_context = BlogsContext("Blog", blogs, getRecentBlogs(), getCategories(), getTags(), getArchives())
    return render(req, 'blog-list.html', {"context": blog_context})

def blogWithSlug(req, blog_year, blog_month, blog_slug):
    logging.info('request MEAT for csrf: %s', req.META.get('CSRF_COOKIE'))
    blog = Blog.objects.get(slug=blog_slug)
    blog_context = BlogContext("Blog", blog, getRecentBlogs(), getCategories(), getTags(), getArchives())
    # if this is a POST request we need to process the form data
    if req.method == 'POST':
        print("HEERE")
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("Form is valid")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()
    return render(req, 'blog-details.html', {"context": blog_context, "form" : form})

def blogArchive(req, blog_year, blog_month):
    blogs = Blog.objects.filter(pub_date__year=blog_year, pub_date__month=blog_month)
    blog_context = BlogsContext("Blog", blogs, getRecentBlogs(), getCategories(), getTags(), getArchives())
    return render(req, 'blog-list.html', {"context": blog_context})

def blogWithTag(req, tag_slug):
    blogs = getBlogsWithPaging(req,Tag.objects.get(slug=tag_slug).blog_set.all())
    blog_context = BlogsContext("Blog", blogs, getRecentBlogs(), getCategories(), getTags(), getArchives())
    return render(req, 'blog-list.html', {"context":blog_context})

def blogWithCategory(req, category_slug):
    blogs = getBlogsWithPaging(req,Category.objects.get(slug=category_slug).blog_set.all())
    blog_context = BlogsContext("Blog", blogs, getRecentBlogs(), getCategories(), getTags(), getArchives())
    return render(req, 'blog-list.html', {"context":blog_context})

def cv(req):
    file_path = os.path.join(settings.STATIC_ROOT, 'CV_NBD.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        return render(req, 'eror-404.html')
    
# Private Methods
def getCategories():
    return Category.objects.annotate(blog_count=Count('blog')).filter(blog_count__gt=0).order_by('-blog_count')

def getTags():
    return Tag.objects.annotate(blog_count=Count('blog')).filter(blog_count__gt=0).order_by('-blog_count')

def getRecentBlogs():
    return Blog.objects.all().order_by('-pub_date')[:7]

def getArchives():
    return Blog.getArchives()

def getBlogsWithPaging(req, blog_list):
    max_paging = 2
    page_no = req.GET.get('page')
    blogs_paginator = Paginator(blog_list, max_paging)
    try:
        blogs = blogs_paginator.page(page_no)
    except PageNotAnInteger:
        blogs = blogs_paginator.page(1)
    except EmptyPage:
        blogs = blogs_paginator.page(blogs_paginator.num_pages)
    return blogs