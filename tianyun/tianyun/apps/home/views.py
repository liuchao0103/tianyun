# -*- coding: utf-8 -*-
__auther__ = 'weixuefeng@lubangame.com'
__version__ = '$Rev$'
__doc__ = 'tianyun home page'

# -*- coding: utf-8 -*-
import logging
import time
import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Q, F
from django.db.models import Sum 
from django.contrib.auth.models import User
from django.conf import settings


@login_required
def index(request):
    return render(request, 'home/index.html', locals())
