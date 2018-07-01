# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from . import models

class AccumulationForm(ModelForm):
    
    def __init__(self, *args, **kw):
        super(AccumulationForm, self).__init__(*args, **kw)
        self.fields['production_id'].label = "版号（产品号）"
        self.fields['production_number'].label = "支数"
        self.fields['coefficient'].label = "系数"
        self.fields['accumulation_number'].label = "积分"
        self.fields['comment'].label = "备注"
    class Meta:
        model = models.Accumulation
        fields = [
            'production_id',
            'production_number',
            'coefficient',
            'accumulation_number',
            'comment'
        ]