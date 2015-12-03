# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='address_1',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='city',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='electronic_signature',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='entity_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='state',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='tin',
            field=encrypted_fields.fields.EncryptedCharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='zip_code',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashuser',
            name='username',
            field=models.CharField(help_text=b'Other Ithacash users can use this to pay you. Simpler is better.', unique=True, max_length=120, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only letters and numbers are allowed')]),
        ),
    ]
