from django.http import HttpResponse
#-*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.shortcuts import render
def home(request):
    text = """<head>
<meta charset=utf-8" />
<title>Test</title>
<link type="text/css" rel="stylesheet" href="static/style.css">
</head>
<body>
<div align="center">
<img src="static/nyan.gif" width="400" height="420" alt="NyanError" />
<h1>WTF go Ahead !</h1>
</div>
</body>
</br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br></br></br>
</br>
</br>
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
</footer>"""
    return HttpResponse(text)
