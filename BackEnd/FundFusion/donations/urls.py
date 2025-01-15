from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonationViewSet, DonationAnalyticsViewSet

router = DefaultRouter()
router.register('donations', DonationViewSet, basename='donation')
router.register('donations-analytics', DonationAnalyticsViewSet, basename='donation-analytics')

urlpatterns = [
    path('', include(router.urls)),
]
