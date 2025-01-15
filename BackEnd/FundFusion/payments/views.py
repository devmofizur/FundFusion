from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from .models import Payment, RecurringDonation
from campaigns.models import Campaign
from .serializers import PaymentSerializer
import logging

logger = logging.getLogger(__name__)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin:
            return Payment.objects.all()
        return Payment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_donation(request):
    try:
        campaign_id = request.data.get('campaign_id')
        amount = request.data.get('amount')

        if not campaign_id or not amount:
            return Response({'error': 'Campaign ID and amount are required.'}, status=status.HTTP_400_BAD_REQUEST)

        campaign = get_object_or_404(Campaign, id=campaign_id, status='approved')
        user = request.user
        campaign.update_amount(amount)

        payment = Payment.objects.create(
            user=user,
            campaign=campaign,
            amount=amount,
            payment_date=now(),
            status='success'
        )

        logger.info(f"User {user.email} donated {amount} to campaign {campaign.title}.")
        return Response({'message': 'Donation successful', 'payment_id': payment.id}, status=status.HTTP_201_CREATED)

    except Exception as e:
        logger.error(f"Error in create_donation: {e}")
        return Response({'error': 'An error occurred while processing the donation.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_recurring_donation(request):
    try:
        campaign_id = request.data.get('campaign_id')
        amount = request.data.get('amount')
        frequency = request.data.get('frequency')

        if not campaign_id or not amount or not frequency:
            return Response({'error': 'Campaign ID, amount, and frequency are required.'}, status=status.HTTP_400_BAD_REQUEST)

        campaign = get_object_or_404(Campaign, id=campaign_id, status='approved')
        user = request.user

        recurring_donation = RecurringDonation.objects.create(
            user=user,
            campaign=campaign,
            amount=amount,
            frequency=frequency,
            next_payment_date=now()
        )

        logger.info(f"User {user.email} set up a recurring donation of {amount} to campaign {campaign.title}.")
        return Response({'message': 'Recurring donation setup successful', 'recurring_donation_id': recurring_donation.id}, status=status.HTTP_201_CREATED)

    except Exception as e:
        logger.error(f"Error in create_recurring_donation: {e}")
        return Response({'error': 'An error occurred while setting up the recurring donation.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def webhook_listener(request):
    try:
        payload = request.data
        transaction_id = payload.get('transaction_id')
        status = payload.get('status')

        if not transaction_id or not status:
            return Response({'error': 'Invalid webhook payload.'}, status=status.HTTP_400_BAD_REQUEST)

        payment = get_object_or_404(Payment, transaction_id=transaction_id)
        payment.status = status
        payment.save()

        logger.info(f"Webhook updated payment {transaction_id} status to {status}.")
        return Response({'message': 'Payment status updated successfully.'}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error in webhook_listener: {e}")
        return Response({'error': 'An error occurred while processing the webhook.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
