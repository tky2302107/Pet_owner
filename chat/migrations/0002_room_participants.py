# Generated by Django 5.1.2 on 2024-10-29 02:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='rooms', to=settings.AUTH_USER_MODEL, verbose_name='Participants'),
        ),
    ]
