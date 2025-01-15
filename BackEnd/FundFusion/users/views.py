from rest_framework import generics, permissions, status
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer
from .serializers import (
    UserSerializer,
    UpdateProfileSerializer,
    ChangePasswordSerializer,
    DonationAnalyticsSerializer
)

User = get_user_model()

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(data=request.data, instance=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        if not check_password(serializer.validated_data['old_password'], user.password):
            return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({'message': 'Password updated successfully'})

class DonationAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        donations = Campaign.objects.filter(donations__user=user)  # Assuming a Donations model exists
        total_donated = donations.aggregate(models.Sum('donations__amount'))['donations__amount__sum'] or 0
        campaigns_supported = donations.values('id').distinct().count()

        data = {
            'total_donated': total_donated,
            'campaigns_supported': campaigns_supported,
        }
        serializer = DonationAnalyticsSerializer(data)
        return Response(serializer.data)
