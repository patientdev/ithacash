# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields
from django.conf import settings
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IthacashUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(help_text=b'Other Ithacash users can use this to pay you. Simpler is better.', unique=True, max_length=120)),
                ('full_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.EmailField(unique=True, max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.DateTimeField(null=True, blank=True)),
                ('most_recent_confirmation_key', models.CharField(max_length=255)),
                ('wants_to_receive_updates', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(related_name='emails', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IthacashAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=20, choices=[(None, b'Select Account Type'), (b'Individual', b'Individual'), (b'Freelancer', b'Freelancer'), (b'Standard Business', b'Standard Business'), (b'Premier Business', b'Premier Business'), (b'Nonprofit', b'Nonprofit')])),
                ('entity_name', models.CharField(max_length=255)),
                ('billing_frequency', models.CharField(default=b'Monthly', max_length=11, choices=[(b'Monthly', b'Monthly'), (b'Semi-Annual', b'Semi-Annual')])),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('tin', encrypted_fields.fields.EncryptedCharField(max_length=255)),
                ('is_ssn', models.BooleanField(default=False)),
                ('phone_mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=255, null=True, blank=True)),
                ('phone_landline', phonenumber_field.modelfields.PhoneNumberField(max_length=255, null=True, blank=True)),
                ('website', models.URLField(max_length=255, null=True, blank=True)),
                ('txt2pay', models.BooleanField(default=False)),
                ('txt2pay_phone', models.BooleanField(default=False)),
                ('electronic_signature', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
