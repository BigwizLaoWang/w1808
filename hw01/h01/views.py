# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import movies

# Create your views here.
def checkList(req):
    data=movies.objects.filter(price__lte=10000)
    result = {
        "list":"HERO MOVIE ",
        "content":data
    }
    return render(req,"MyMovie.html",result)
