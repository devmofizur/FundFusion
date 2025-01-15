from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

# Validator to ensure file size is within limit
def validate_file_size(value):
    filesize = value.size
    if filesize > 10 * 1024 * 1024:  # 10MB
        raise ValidationError("Maximum file size is 10MB")

class Campaign(models.Model):
    # Category choices for campaigns
    CATEGORY_CHOICES = [
        ('Medical', 'Medical'),
        ('Education', 'Education'),
        ('Disaster Relief', 'Disaster Relief'),
        ('Environmental Conservation', 'Environmental Conservation'),
        ('Social Justice', 'Social Justice'),
        ('Animal Welfare', 'Animal Welfare'),
        ('Community Development', 'Community Development'),
        ('Non-profit Support', 'Non-profit Support'),
        ('Arts and Culture', 'Arts and Culture'),
        ('Other', 'Other'),
    ]
    # Status choices for campaigns
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]

    # Fields for the Campaign model
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(10.00)]  # Minimum goal amount is $10
    )
    current_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    location = models.CharField(max_length=100)
    banner_image = models.ImageField(
        upload_to='campaign_banners/',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
            validate_file_size
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    contact_info = models.EmailField()
    story = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    total_donors = models.PositiveIntegerField(default=0)

    # Metadata
    class Meta:
        indexes = [
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['creator', 'status']),
            models.Index(fields=['category', 'status']),
        ]

    # Method to safely update campaign amount
    def update_amount(self, donation_amount):
        if self.status != 'approved':
            raise ValidationError("Cannot donate to unapproved campaign.")

        # Atomic update of current amount and total donors
        self.current_amount = models.F('current_amount') + donation_amount
        self.total_donors = models.F('total_donors') + 1
        self.save()

        # Refresh to get the updated values
        self.refresh_from_db()

        # Check if campaign goal is reached
        if self.current_amount >= self.goal_amount and self.status != 'completed':
            self.status = 'completed'
            self.save()

    def __str__(self):
        return self.title

class CampaignRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=Campaign.CATEGORY_CHOICES)
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
