from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, CampaignRequestView

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')

urlpatterns = [
    path('api/', include(router.urls)),  # Note the 'api/' prefix
    path('campaign-requests/', CampaignRequestView.as_view(), name='campaign-request'),
]