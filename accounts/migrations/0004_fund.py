# Generated by Django 5.1.3 on 2024-11-14 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_sum', models.IntegerField(default=0)),
            ],
        ),
    ]
