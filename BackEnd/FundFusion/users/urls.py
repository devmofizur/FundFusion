from django.urls import path
from .views import (
    UserProfileView,
    ChangePasswordView,
    DonationAnalyticsView,
)

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/donation-analytics/', DonationAnalyticsView.as_view(), name='donation-analytics'),
]
