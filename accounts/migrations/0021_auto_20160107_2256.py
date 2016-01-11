# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20160107_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='is_ssn',
            field=models.BooleanField(default=True, choices=[(True, b'SSN'), (False, b'EIN')]),
        ),
    ]
