from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'store/home.html')


def wholesale_view(request):
    return render(request, 'store/wholesale.html')


def about_view(request):
    return render(request, 'store/about.html')


def contact_view(request):
    return render(request, 'store/contact.html')

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products})

@login_required
def account_view(request):
    return render(request, 'store/account.html')
