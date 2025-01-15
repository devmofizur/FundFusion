from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'user', 'campaign', 'amount', 'donated_at']
        read_only_fields = ['id', 'donated_at']
