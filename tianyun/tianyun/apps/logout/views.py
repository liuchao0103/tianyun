# -*- coding: utf-8 -*-
__author__ = 'weixuefeng@lubangame.com'
__version__ = '$Rev$'
__doc__ = """  """

import logging
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
