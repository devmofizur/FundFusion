import pytest
from apps.payments.serializers import PaymentSerializer
from apps.users.models import CustomUser
from apps.campaigns.models import Campaign
from django.utils import timezone

@pytest.mark.django_db
class TestPaymentSerializer:
    def setup_method(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.campaign = Campaign.objects.create(
            title="Test Campaign",
            description="This is a test campaign",
            goal_amount=1000,
            end_date=timezone.now() + timezone.timedelta(days=30),
            creator=self.user
        )

    def test_valid_payment_serializer(self):
        payment_data = {
            'user': self.user.id,
            'campaign': self.campaign.id,
            'amount': 100,
            'transaction_id': 'TEST123',
            'status': 'completed',
            'payment_method': 'bKash'
        }
        serializer = PaymentSerializer(data=payment_data)
        assert serializer.is_valid()

    def test_invalid_amount(self):
        payment_data = {
            'user': self.user.id,
            'campaign': self.campaign.id,
            'amount': -100,  # Invalid negative amount
            'transaction_id': 'TEST123',
            'status': 'completed',
            'payment_method': 'bKash'
        }
        serializer = PaymentSerializer(data=payment_data)
        assert not serializer.is_valid()
        assert 'amount' in serializer.errors
