# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20151218_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='address_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='electronic_signature',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='phone_landline',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='state',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='zip_code',
            field=models.CharField(max_length=255),
        ),
    ]
