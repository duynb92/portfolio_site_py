# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *

# Create your views here.
def index(req):
    context = HomeContext("Home", Facade.getSkills(), Facade.getHobbies())
    return render(req, 'index.html', context=vars(context))

def profile(req):
    profile_context = ProfileContext("Profile", Facade.getProfiles())
    return render(req, 'profile.html', context=vars(profile_context))

def portfolio(req):
    portfolio_context = PortfolioContext("Portfolio", Facade.getProjects())
    return render(req, 'portfolio-gird-3.html', context=vars(portfolio_context))

def service(req):
    service_context = ServiceContext("Services", Facade.getServices())
    return render(req, 'services.html', context=vars(service_context))

def contact(req):
    context = BaseContext("Contact")
    return render(req, 'contact-3.html', context=vars(context))

def blog(req):
    blog_context = BlogContext("Blog", [])
    return render(req, 'blog.html', context=vars(blog_context))