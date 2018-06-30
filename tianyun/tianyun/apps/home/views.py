# -*- coding: utf-8 -*-
__auther__ = 'weixuefeng@lubangame.com'
__version__ = '$Rev$'
__doc__ = 'tianyun home page'

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html', locals())
