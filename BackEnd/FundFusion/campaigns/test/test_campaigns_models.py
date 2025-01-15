import pytest
from django.utils import timezone
from apps.campaigns.models import Campaign
from apps.users.models import CustomUser

@pytest.mark.django_db
class TestCampaignModel:
    def test_campaign_creation(self):
        user = CustomUser.objects.create_user(username='testuser', password='12345')
        campaign = Campaign.objects.create(
            title="Test Campaign",
            description="This is a test campaign",
            goal_amount=1000,
            end_date=timezone.now() + timezone.timedelta(days=30),
            creator=user
        )
        assert campaign.title == "Test Campaign"
        assert campaign.current_amount == 0
        assert campaign.is_approved == False

    def test_campaign_str_representation(self):
        user = CustomUser.objects.create_user(username='testuser', password='12345')
        campaign = Campaign.objects.create(
            title="Test Campaign",
            description="This is a test campaign",
            goal_amount=1000,
            end_date=timezone.now() + timezone.timedelta(days=30),
            creator=user
        )
        assert str(campaign) == "Test Campaign"
