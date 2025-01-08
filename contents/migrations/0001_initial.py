# Generated by Django 5.1.2 on 2025-01-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('follow', models.IntegerField(verbose_name='アカウントID')),
                ('follow_name', models.CharField(blank=True, default='', max_length=128, verbose_name='アカウント名')),
                ('follow_er', models.IntegerField(verbose_name='アカウントID')),
                ('follow_er_name', models.CharField(blank=True, default='', max_length=128, verbose_name='アカウント名')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30, verbose_name='病院名')),
                ('address', models.CharField(default='', max_length=50, verbose_name='住所')),
                ('detail', models.CharField(default='', max_length=128, verbose_name='詳細')),
                ('hp', models.CharField(blank=True, default='', max_length=300, verbose_name='ホームページ')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='日時')),
                ('title', models.CharField(default='', max_length=30, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
            ],
        ),
    ]
