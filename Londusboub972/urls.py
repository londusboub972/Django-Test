from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Londusboub972.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^contact/', 'contact.views.contact'),
    url(r'^secret/', 'secret.views.secret'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home'),

)
