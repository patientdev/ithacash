# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
import encrypted_fields.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='entity_name',
            field=models.CharField(default=datetime.datetime(2016, 1, 7, 20, 6, 28, 970067, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='tin',
            field=encrypted_fields.fields.EncryptedCharField(default=0, help_text=b'This is a secure site. Your information will not be seen by anyone internally, distributed, or shared.', max_length=255, validators=[django.core.validators.MinLengthValidator(9, b'This should be exactly 9 numbers. (It has %(show_value)d)'), django.core.validators.MaxLengthValidator(9, b'This should be exactly 9 numbers. (It has %(show_value)d)')]),
            preserve_default=False,
        ),
    ]
