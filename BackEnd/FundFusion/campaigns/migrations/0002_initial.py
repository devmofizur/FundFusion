# Generated by Django 4.2.7 on 2024-11-26 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='campaign',
            index=models.Index(fields=['status', 'created_at'], name='campaigns_c_status_6076a2_idx'),
        ),
        migrations.AddIndex(
            model_name='campaign',
            index=models.Index(fields=['creator', 'status'], name='campaigns_c_creator_ba2d33_idx'),
        ),
        migrations.AddIndex(
            model_name='campaign',
            index=models.Index(fields=['category', 'status'], name='campaigns_c_categor_239956_idx'),
        ),
    ]
