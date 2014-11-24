from django.http import HttpResponse
#-*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.shortcuts import render


from django import forms

class ContactForm(forms.Form):
    mailler = forms.EmailField(label="Your mail")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mailler = form.cleaned_data['mailler']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send = True
    else:
        form = ContactForm()
    return render(request, 'contact.html', locals())

