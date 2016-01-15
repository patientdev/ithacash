# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20151218_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='address_1',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='address_2',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='city',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='electronic_signature',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='phone_landline',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='phone_mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='state',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='tin',
            field=encrypted_fields.fields.EncryptedCharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='website',
            field=models.URLField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='zip_code',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
