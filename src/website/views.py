from django.conf import settings
from django.contrib import  messages
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect

from .forms import ContactForm
from .models import Contact 

def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
       instance = form.save(commit=False)
       instance.save()

       form_email = form.cleaned_data.get("email")
       form_name = form.cleaned_data.get("first_name")+" "+form.cleaned_data.get("last_name")
       form_message = form.cleaned_data.get("message")
       form_date = form.cleaned_data.get("date")

       subject = 'Contact Form Notification'
       from_email = settings.EMAIL_HOST_USER
       body  = 'Name: %s<br/>Contact: %s<br/>Request Date: %s<br/>Message: %s<br/>'%(form_name, form_email, form_date, form_message)
       to = 'ryusukelavalla@gmail.com'    
       html_content = body
       text_content = 'This is an example'
       msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
       msg.attach_alternative(html_content, "text/html")
       msg.send()
        
       messages.success(request, "Thank you very much. Your request has been submitted successfully." )
       return HttpResponseRedirect("/")

    context ={
             "form":form,
    }
    return render(request,"index.html", context)
