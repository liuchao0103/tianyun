# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(label=_("UserName"), required=True)
    password = forms.CharField(widget=forms.PasswordInput(),label=_("Password"), required=True)
