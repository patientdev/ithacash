# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='entity_name',
            field=models.CharField(default=datetime.datetime(2016, 1, 15, 22, 46, 9, 235423, tzinfo=utc), max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ithacashuser',
            name='username',
            field=models.CharField(help_text=b'Other Ithacash users can use this to pay you. Simpler is better.', max_length=120, unique=True, null=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only letters and numbers are allowed')]),
        ),
    ]
