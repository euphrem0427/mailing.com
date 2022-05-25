from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from sendmail.forms import SendMailForm
from mailling.settings import EMAIL_HOST_USER
# Create your views here.

def index(request):
    form = SendMailForm()
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recepient = str(form['receiver'].value())
            send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            
            return redirect('success')
            
    context = {}
    return render(request, 'index.html', context)

def success(request):
    context = {}
    return render(request, 'success.html', context)