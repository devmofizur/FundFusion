from django.db import models
from users.models import User
from campaigns.models import Campaign
from django.utils.timezone import now, timedelta


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='payments', db_index=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True, db_index=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ])
    payment_method = models.CharField(max_length=50)  # e.g., bKash, Rocket, credit card, etc.

    def __str__(self):
        return f"{self.amount} for {self.campaign.title}"

    def mark_completed(self):
        self.status = 'completed'
        self.save()

    def mark_failed(self):
        self.status = 'failed'
        self.save()


class RecurringDonation(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recurring_donations')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='recurring_donations', db_index=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    next_payment_date = models.DateTimeField()
    active = models.BooleanField(default=True)  # Indicates whether the recurring donation is active
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} every {self.frequency} for {self.campaign.title}"

    def schedule_next_payment(self):
        """Update the next payment date based on the frequency."""
        if self.frequency == 'daily':
            self.next_payment_date += timedelta(days=1)
        elif self.frequency == 'weekly':
            self.next_payment_date += timedelta(weeks=1)
        elif self.frequency == 'monthly':
            self.next_payment_date += timedelta(days=30)  # Approximation for months
        self.save()

    def cancel(self):
        """Deactivate the recurring donation."""
        self.active = False
        self.save()
