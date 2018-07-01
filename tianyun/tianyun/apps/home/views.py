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

from . import forms
from . import models
from utils import http


@login_required
def index(request):
    records = models.Accumulation.objects.filter(user_id=request.user.id)
    return render(request, 'home/index.html', locals())

@login_required
def show_add_view(request):
    form = forms.AccumulationForm
    return render(request, 'home/add-accumulation.html', locals())
    
@login_required
def add_post(request):
    try:
        instance = models.Accumulation()
        instance.user_id = request.user.id
        form = forms.AccumulationForm(request.POST, instance=instance)
        if not form.is_valid():
            return render(request, "home/add-accumulation.html", locals()) 
        instance = form.save(commit=True)
        instance.save()
        return http.HttpResponseRedirect('/')
    except Exception, inst:
        return http.HttpResponseServerError()

