from django.urls import path
from .views import home_view, wholesale_view, about_view, contact_view, product_list_view, account_view

urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', product_list_view, name='shop'),
    path('wholesale/', wholesale_view, name='wholesale'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('account/', account_view, name='account'),
]
