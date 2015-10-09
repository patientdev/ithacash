# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashuser',
            name='username',
            field=models.CharField(help_text=b'Other Ithacash users can use this to pay you. Simpler is better.', unique=True, max_length=120, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
