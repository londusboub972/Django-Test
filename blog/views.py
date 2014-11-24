from django.http import HttpResponse
#-*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.shortcuts import render

def home(request):
    text = """<head>
<meta charset=utf-8" />
<title>Django first page</title>
<link type="text/css" rel="stylesheet" href="static/home/style.css">
</head>
<body>
<div align="center">
<img src="static/home/nyan.gif" width="400" height="420" alt="NyanError" />
 <a href="secret"> <h1>Hey wanna get high?</h1> </a>
</div>
</body>

<footer>
</br>
</br>
</br>
<div align="center">
Copyright 2014
</div>
</br>
</br>
</br>
</footer>
"""

    return HttpResponse(text)

