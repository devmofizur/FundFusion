from rest_framework import viewsets, permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import Campaign, CampaignRequest
from .serializers import CampaignSerializer, CampaignRequestSerializer
from django.db.models import Q


class CampaignRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CampaignRequestSerializer(data=request.data)
        if serializer.is_valid():
            campaign_request = serializer.save(requester=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if request.user.is_staff:
            campaign_requests = CampaignRequest.objects.all()
        else:
            campaign_requests = CampaignRequest.objects.filter(requester=request.user)
        serializer = CampaignRequestSerializer(campaign_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter campaigns based on user roles (staff users can see all campaigns)
        if self.request.user.is_staff:
            return Campaign.objects.all()
        return Campaign.objects.filter(
            Q(status='approved') | Q(creator=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user, status='pending')

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        campaign = self.get_object()
        campaign.status = 'approved'
        campaign.save()
        serializer = self.get_serializer(campaign)
        return Response({'status': 'approved', 'campaign': serializer.data})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def reject(self, request, pk=None):
        campaign = self.get_object()
        campaign.status = 'rejected'
        campaign.save()
        return Response({'status': 'rejected'})

    @action(detail=True, methods=['get'])
    def increment_views(self, request, pk=None):
        campaign = self.get_object()
        campaign.views += 1
        campaign.save()
        return Response({'message': 'Views incremented', 'views': campaign.views})

    def retrieve(self, request, *args, **kwargs):
        # Custom behavior for retrieving a campaign
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def my_campaigns(self, request):
        # Returns campaigns created by the logged-in user
        campaigns = Campaign.objects.filter(creator=request.user)
        serializer = self.get_serializer(campaigns, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        # Returns campaigns filtered by category
        categories = Campaign.CATEGORY_CHOICES
        result = {}
        for category_key, category_name in categories:
            campaigns = Campaign.objects.filter(category=category_key, status='approved')
            result[category_name] = self.get_serializer(campaigns, many=True).data
        return Response(result)

    @action(detail=False, methods=['get'])
    def search(self, request):
        # Custom search functionality for campaigns
        query = request.query_params.get('query', '')
        status_filter = request.query_params.get('status', None)
        min_goal = request.query_params.get('min_goal', None)
        max_goal = request.query_params.get('max_goal', None)

        filters = Q(title__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query)
        if status_filter:
            filters &= Q(status=status_filter)
        if min_goal:
            filters &= Q(goal_amount__gte=min_goal)
        if max_goal:
            filters &= Q(goal_amount__lte=max_goal)

        campaigns = Campaign.objects.filter(filters)
        serializer = self.get_serializer(campaigns, many=True)
        return Response(serializer.data)