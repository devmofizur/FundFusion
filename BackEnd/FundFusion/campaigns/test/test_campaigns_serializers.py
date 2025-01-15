import pytest
from django.utils import timezone
from apps.campaigns.models import Campaign
from apps.campaigns.serializers import CampaignSerializer
from apps.users.models import CustomUser

@pytest.mark.django_db
class TestCampaignSerializer:
    def test_valid_campaign_serializer(self):
        user = CustomUser.objects.create_user(username='testuser', password='12345')
        campaign_data = {
            'title': 'Test Campaign',
            'description': 'This is a test campaign',
            'goal_amount': 1000,
            'end_date': timezone.now() + timezone.timedelta(days=30),
            'creator': user.id
        }
        serializer = CampaignSerializer(data=campaign_data)
        assert serializer.is_valid()

    def test_invalid_goal_amount(self):
        user = CustomUser.objects.create_user(username='testuser', password='12345')
        campaign_data = {
            'title': 'Test Campaign',
            'description': 'This is a test campaign',
            'goal_amount': -1000,  # Invalid negative amount
            'end_date': timezone.now() + timezone.timedelta(days=30),
            'creator': user.id
        }
        serializer = CampaignSerializer(data=campaign_data)
        assert not serializer.is_valid()
        assert 'goal_amount' in serializer.errors
        assert 'Goal amount must be greater than zero.' in str(serializer.errors['goal_amount'])

