import pytest
from apps.payments.models import Payment
from apps.users.models import CustomUser
from apps.campaigns.models import Campaign
from django.utils import timezone

@pytest.mark.django_db
class TestPaymentModel:
    def setup_method(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.campaign = Campaign.objects.create(
            title="Test Campaign",
            description="This is a test campaign",
            goal_amount=1000,
            end_date=timezone.now() + timezone.timedelta(days=30),
            creator=self.user
        )

    def test_payment_creation(self):
        payment = Payment.objects.create(
            user=self.user,
            campaign=self.campaign,
            amount=100,
            transaction_id='TEST123',
            status='completed',
            payment_method='bKash'
        )
        assert payment.amount == 100
        assert payment.status == 'completed'
        assert payment.payment_method == 'bKash'

    def test_payment_str_representation(self):
        payment = Payment.objects.create(
            user=self.user,
            campaign=self.campaign,
            amount=100,
            transaction_id='TEST123',
            status='completed',
            payment_method='bKash'
        )
        assert str(payment) == f"100 for {self.campaign.title}"
