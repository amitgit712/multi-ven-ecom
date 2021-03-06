# Generated by Django 4.0.3 on 2022-03-17 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('shop_name', models.CharField(max_length=250, null=True, verbose_name='shop name')),
                ('description', models.TextField(null=True, verbose_name='description')),
                ('phone_number', models.CharField(default=0, max_length=11, verbose_name='phone number')),
                ('is_account_closed', models.BooleanField(default=False)),
                ('is_suspended', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL, verbose_name='Create by')),
            ],
        ),
    ]
