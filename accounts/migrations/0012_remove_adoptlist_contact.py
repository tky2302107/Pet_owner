# Generated by Django 5.1.2 on 2025-01-07 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_hp_adoptlist_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptlist',
            name='contact',
        ),
    ]
