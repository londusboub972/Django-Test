from django.http import HttpResponse
#-*- coding: utf-8 -*-
from django.conf.urls.static import static
from django.core.mail import send_mail
from django import forms
from django.shortcuts import render

class ContactForm(forms.Form):
    sender = forms.EmailField(label="Your mail")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send = True
    
            recipients = ['test']

            send_mail(subject, message, sender, recipients)
    else:
        form = ContactForm()
    return render(request, 'contact.html', locals())



