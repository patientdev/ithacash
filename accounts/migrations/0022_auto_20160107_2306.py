# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20160107_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='is_ssn',
            field=models.BooleanField(choices=[(True, b'SSN'), (False, b'EIN')]),
        ),
    ]
