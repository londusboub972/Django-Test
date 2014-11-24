from django.http import HttpResponse
#-*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.shortcuts import render

def secret(request):
    text = """<head>
<meta charset=utf-8" />
<title>Secret Page</title>
<link type="text/css" rel="stylesheet" href="/static/style.css">
</head>
<div align="center">
<h1>Now you high bro' !</h1>
<iframe width="420" height="315" src="//www.youtube.com/embed/zHU2RlSCdxU" frameborder="0" allowfullscreen></iframe></br>
Copyright 2014
</div>
</br>
</br>
</br>
</footer>
"""

    return HttpResponse(text)
