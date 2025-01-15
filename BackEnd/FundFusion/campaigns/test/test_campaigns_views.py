import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.campaigns.models import Campaign
from apps.users.models import CustomUser
from django.utils import timezone

@pytest.mark.django_db
class TestCampaignViews:
    def setup_method(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.admin = CustomUser.objects.create_superuser(username='admin', password='admin123')
        self.campaign_data = {
            'title': 'Test Campaign',
            'description': 'This is a test campaign',
            'goal_amount': 1000,
            'end_date': (timezone.now() + timezone.timedelta(days=30)).isoformat(),
        }

    def test_create_campaign(self):
        self.client.force_authenticate(user=self.user)
        campaign_data = {
            'title': 'Test Campaign',
            'description': 'This is a test campaign',
            'goal_amount': 1000,
            'end_date': (timezone.now() + timezone.timedelta(days=30)).isoformat(),
        }
        response = self.client.post(reverse('campaign-list'), campaign_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Campaign.objects.count() == 1
        campaign = Campaign.objects.get()
        assert campaign.title == 'Test Campaign'
        assert campaign.creator == self.user

    def test_list_campaigns(self):
        Campaign.objects.create(creator=self.user, **self.campaign_data)
        response = self.client.get(reverse('campaign-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_approve_campaign(self):
        campaign = Campaign.objects.create(creator=self.user, **self.campaign_data)
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(reverse('campaign-approve', kwargs={'pk': campaign.id}))
        assert response.status_code == status.HTTP_200_OK
        campaign.refresh_from_db()
        assert campaign.is_approved == True

    def test_non_admin_cannot_approve_campaign(self):
        campaign = Campaign.objects.create(creator=self.user, **self.campaign_data)
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('campaign-approve', kwargs={'pk': campaign.id}))
        assert response.status_code == status.HTTP_403_FORBIDDEN
