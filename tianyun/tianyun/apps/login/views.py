
import logging

from django.shortcuts import render,redirect
from django.forms.forms import NON_FIELD_ERRORS
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from . import forms
from utils import http

logger = logging.getLogger(__name__)

def show_login_view(request):
    form = forms.LoginForm()
    return render(request, "login/index.html", locals())

#TODO: http_post_required
def post_login(request):
    try:
        form = forms.LoginForm(request.POST)
        if not form.is_valid():
            form._errors[NON_FIELD_ERRORS] = form.error_class([_("Error")])
            return render(request, "login/index.html", locals()) 
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            form._errors[NON_FIELD_ERRORS] = form.error_class([_("No User")])
            return render(request, "login/index.html", locals()) 
        login(request, user)
        return http.HttpResponseRedirect('/')
    except Exception, inst:
        return http.HttpResponseServerError()
