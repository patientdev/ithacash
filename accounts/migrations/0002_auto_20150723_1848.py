# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IthacashAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=20, choices=[(None, b'Who are you?'), (b'Individual', b'Individual'), (b'Freelancer', b'Freelancer'), (b'Business', b'Business'), (b'Nonprofit', b'Nonprofit')])),
                ('name_business', models.CharField(max_length=255)),
                ('name_contact', models.CharField(max_length=255)),
                ('name_login', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(max_length=255, null=True, blank=True)),
                ('address_city', models.CharField(default=b'Ithaca', max_length=255)),
                ('address_state', models.CharField(default=b'NY', max_length=255)),
                ('address_zip_code', models.CharField(default=b'14850', max_length=255)),
                ('tin', encrypted_fields.fields.EncryptedCharField(max_length=255)),
                ('phone_mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=255, null=True, blank=True)),
                ('phone_landline', phonenumber_field.modelfields.PhoneNumberField(max_length=255, null=True, blank=True)),
                ('website', models.URLField(max_length=255, null=True, blank=True)),
                ('txt2pay', models.BooleanField()),
                ('txt2pay_phone', models.BooleanField()),
                ('electronic_signature', models.CharField(max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='wants_to_receive_updates',
            field=models.BooleanField(default=False),
        ),
    ]
