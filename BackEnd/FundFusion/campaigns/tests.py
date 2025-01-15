from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from .models import Campaign
from datetime import timedelta

User = get_user_model()


class CampaignAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )

        # Create an API client
        self.client = APIClient()

        # Authenticate the user
        self.client.force_authenticate(user=self.user)

        # Prepare valid campaign data
        self.valid_campaign_data = {
            'title': 'Test Education Campaign',
            'description': 'A comprehensive campaign to support education',
            'goal_amount': 5000.00,
            'location': 'New York',
            'category': 'Education',
            'end_date': (timezone.now() + timedelta(days=30)).isoformat(),
            'contact_info': 'campaign@example.com',
        }

    def test_create_campaign_success(self):
        """
        Test successful campaign creation
        """
        response = self.client.post('/api/campaigns/', self.valid_campaign_data, format='json')

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify campaign was created in database
        campaign = Campaign.objects.get(title='Test Education Campaign')
        self.assertIsNotNone(campaign)

        # Check specific fields
        self.assertEqual(float(campaign.goal_amount), 5000.00)
        self.assertEqual(campaign.creator, self.user)
        self.assertEqual(campaign.status, 'pending')

    def test_create_campaign_invalid_goal_amount(self):
        """
        Test campaign creation with invalid goal amount
        """
        invalid_data = self.valid_campaign_data.copy()
        invalid_data['goal_amount'] = 5.00  # Below minimum

        response = self.client.post('/api/campaigns/', invalid_data, format='json')

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify no campaign was created
        self.assertEqual(Campaign.objects.count(), 0)

    def test_create_campaign_past_end_date(self):
        """
        Test campaign creation with past end date
        """
        invalid_data = self.valid_campaign_data.copy()
        invalid_data['end_date'] = (timezone.now() - timedelta(days=1)).isoformat()

        response = self.client.post('/api/campaigns/', invalid_data, format='json')

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify no campaign was created
        self.assertEqual(Campaign.objects.count(), 0)

    def test_create_campaign_missing_required_fields(self):
        """
        Test campaign creation with missing required fields
        """
        # Remove a required field
        incomplete_data = self.valid_campaign_data.copy()
        del incomplete_data['title']

        response = self.client.post('/api/campaigns/', incomplete_data, format='json')

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Verify no campaign was created
        self.assertEqual(Campaign.objects.count(), 0)

    def test_create_campaign_unauthenticated(self):
        """
        Test campaign creation without authentication
        """
        # Logout the user
        self.client.force_authenticate(user=None)

        response = self.client.post('/api/campaigns/', self.valid_campaign_data, format='json')

        # Check response status (should be unauthorized)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Verify no campaign was created
        self.assertEqual(Campaign.objects.count(), 0)

    def test_campaign_default_values(self):
        """
        Test default values when creating a campaign
        """
        response = self.client.post('/api/campaigns/', self.valid_campaign_data, format='json')

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the created campaign
        campaign = Campaign.objects.get(title='Test Education Campaign')

        # Check default values
        self.assertEqual(campaign.current_amount, 0)
        self.assertEqual(campaign.views, 0)
        self.assertEqual(campaign.total_donors, 0)
        self.assertEqual(campaign.status, 'pending')
