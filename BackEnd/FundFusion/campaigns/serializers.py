from rest_framework import serializers
from .models import Campaign, CampaignRequest
from django.core.exceptions import ValidationError
from django.utils import timezone


class CampaignSerializer(serializers.ModelSerializer):
    goalAmount = serializers.DecimalField(
        source='goal_amount',
        max_digits=10,
        decimal_places=2,
        required=True
    )
    bannerImage = serializers.ImageField(
        source='banner_image',
        required=False
    )
    contactInfo = serializers.EmailField(
        source='contact_info',
        required=True
    )
    endDate = serializers.DateTimeField(
        source='end_date',
        required=True
    )
    documents = serializers.ListField(
        child=serializers.FileField(
            max_length=100000,
            allow_empty_file=False,
            use_url=False
        ),
        required=False,
        write_only=True
    )

    class Meta:
        model = Campaign
        fields = [
            'id', 'title', 'description', 'goalAmount', 'location',
            'category', 'endDate', 'contactInfo', 'story',
            'bannerImage', 'documents'
        ]
        read_only_fields = ['current_amount', 'views', 'status', 'creator']

    def validate(self, data):
        # Validate goal amount
        goal_amount = data.get('goal_amount', 0)
        if goal_amount < 10:
            raise serializers.ValidationError({"goalAmount": "Goal amount must be at least $10"})

        # Validate end date
        end_date = data.get('end_date')
        if end_date and end_date <= timezone.now():
            raise serializers.ValidationError({"endDate": "End date must be in the future"})

        # Validate banner image size
        banner_image = data.get('banner_image')
        if banner_image:
            if banner_image.size > 10 * 1024 * 1024:  # 10MB
                raise serializers.ValidationError({"bannerImage": "Banner image must be less than 10MB"})

        return data

    def create(self, validated_data):
        # Handle potential additional fields from frontend
        documents = validated_data.pop('documents', None)
        # Get the user from the context
        user = self.context['request'].user
        # Create the campaign
        campaign = Campaign.objects.create(
            creator=user,
            **validated_data
        )
        # Placeholder for document handling
        if documents:
            for doc in documents:
                print(f"Document received: {doc.name}")
        return campaign

class CampaignRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignRequest
        fields = ['id', 'title', 'description', 'goal_amount', 'location', 'category', 'requester', 'requested_at']
        read_only_fields = ['requester', 'requested_at']

        def perform_create(self, serializer):
            serializer.save(creator=self.request.user, status='pending')
