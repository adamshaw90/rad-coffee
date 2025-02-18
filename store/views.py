from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    return render(request, 'store/home.html')


def wholesale_view(request):
    return render(request, 'store/wholesale.html')


def about_view(request):
    return render(request, 'store/about.html')


def contact_view(request):  # Make sure this exists!
    return render(request, 'store/contact.html')
