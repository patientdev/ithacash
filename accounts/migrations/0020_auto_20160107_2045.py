# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20160107_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='entity_name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='is_ssn',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='tin',
            field=encrypted_fields.fields.EncryptedCharField(blank=True, help_text=b'This is a secure site. Your Tax ID # will not be seen by anyone internally, distributed, or shared.', max_length=255, validators=[django.core.validators.MinLengthValidator(9, b'This should be exactly 9 numbers. (It has %(show_value)d)'), django.core.validators.MaxLengthValidator(9, b'This should be exactly 9 numbers. (It has %(show_value)d)')]),
        ),
    ]
