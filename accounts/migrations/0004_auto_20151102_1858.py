# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150929_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashuser',
            name='username',
            field=models.CharField(help_text=b'Other Ithacash users can use this to pay you. Simpler is better.', unique=True, max_length=120, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only letters and numbers are allowed')]),
        ),
    ]
