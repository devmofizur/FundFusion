import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.payments.models import Payment
from apps.users.models import CustomUser
from apps.campaigns.models import Campaign
from django.utils import timezone

@pytest.mark.django_db
class TestPaymentViews:
    def setup_method(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.admin = CustomUser.objects.create_superuser(username='admin', password='admin123')
        self.campaign = Campaign.objects.create(
            title="Test Campaign",
            description="This is a test campaign",
            goal_amount=1000,
            end_date=timezone.now() + timezone.timedelta(days=30),
            creator=self.user
        )  # Save the campaign object
        self.payment_data = {
            'campaign': self.campaign.id,
            'amount': 100,
            'transaction_id': 'TEST123',
            'status': 'completed',
            'payment_method': 'bKash'
        }

    def test_create_payment(self):
        self.client.force_authenticate(user=self.user)
        payment_data = {
            'campaign': self.campaign.id,
            'amount': 100,
            'transaction_id': 'TEST123',
            'status': 'completed',
            'payment_method': 'bKash'
        }
        response = self.client.post(reverse('payment-list'), payment_data)
        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")

        assert response.status_code == status.HTTP_201_CREATED, f"Unexpected status code: {response.status_code}, data: {response.data}"
        assert Payment.objects.count() == 1, f"Expected 1 payment, got {Payment.objects.count()}"

        payment = Payment.objects.first()
        print(f"Created payment: {payment}")
        print(f"Payment campaign: {payment.campaign}")
        print(f"Payment user: {payment.user}")

        assert payment.amount == 100
        assert payment.campaign == self.campaign
        assert payment.user == self.user

        self.campaign.refresh_from_db()
        assert self.campaign.current_amount == 100

    def test_list_user_payments(self):
        payment = Payment.objects.create(
            user=self.user,
            campaign=self.campaign,
            amount=100,
            transaction_id='TEST123',
            status='completed',
            payment_method='bKash'
        )
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('payment-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_admin_list_all_payments(self):
        payment = Payment.objects.create(
            user=self.user,
            campaign=self.campaign,
            amount=100,
            transaction_id='TEST123',
            status='completed',
            payment_method='bKash'
        )
        print(f"Created payment: {payment}")
        print(f"Total payments in DB: {Payment.objects.count()}")

        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse('payment-list'))
        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")

        assert response.status_code == status.HTTP_200_OK, f"Unexpected status code: {response.status_code}, data: {response.data}"
        assert len(response.data) == 1, f"Expected 1 payment, got {len(response.data)}"
        assert Payment.objects.count() == 1, f"Expected 1 payment in database, got {Payment.objects.count()}"

    def test_user_cannot_see_others_payments(self):
        other_user = CustomUser.objects.create_user(username='otheruser', password='12345')
        payment = Payment.objects.create(
            user=other_user,
            campaign=self.campaign,
            amount=100,
            transaction_id='TEST123',
            status='completed',
            payment_method='bKash'
        )
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('payment-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 0
