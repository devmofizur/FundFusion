from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Only show the username
    campaign = serializers.ReadOnlyField(source='campaign.title')  # Only show the campaign title

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['payment_date', 'transaction_id', 'status']  # Fields managed by the payment system


    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Payment amount must be greater than zero.")
        return value  # Validation for positive payment amounts

    def validate_transaction_id(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Transaction ID must be alphanumeric.")
        return value  # Validation for valid transaction IDs
