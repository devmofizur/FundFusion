from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from campaigns.models import Campaign

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone', 'date_joined', 'is_admin')
        read_only_fields = ('id', 'email', 'date_joined')

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone')

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

class DonationAnalyticsSerializer(serializers.Serializer):
    total_donated = serializers.DecimalField(max_digits=10, decimal_places=2)
    campaigns_supported = serializers.IntegerField()
