from django.urls import path
from .views import create_donation, create_recurring_donation, webhook_listener

urlpatterns = [
    path('donate/', create_donation, name='create_donation'),
    path('donate/recurring/', create_recurring_donation, name='create_recurring_donation'),
    path('webhook/', webhook_listener, name='webhook_listener'),
]
