# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='city',
            field=models.CharField(max_length=255),
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
        migrations.AlterField(
            model_name='ithacashuser',
            name='username',
            field=models.CharField(help_text=b'Other Ithacash users can use this to pay you. Simpler is better.', unique=True, max_length=120),
        ),
    ]
