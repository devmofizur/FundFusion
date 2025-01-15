from rest_framework import viewsets, permissions, status
from django.db import models
from rest_framework.response import Response
from .models import Donation
from .serializers import DonationSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        # List donations by the logged-in user
        queryset = Donation.objects.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class DonationAnalyticsViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Analytics for donations made by the user
        user = request.user
        total_donated = Donation.objects.filter(user=user).aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        campaigns_supported = Donation.objects.filter(user=user).values(
            'campaign_id'
        ).distinct().count()

        data = {
            'total_donated': total_donated,
            'campaigns_supported': campaigns_supported,
        }
        return Response(data)
