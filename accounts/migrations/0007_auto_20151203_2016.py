# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20151201_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='account_type',
            field=models.CharField(max_length=20, choices=[(b'Individual', b'Individual'), (b'Freelancer', b'Freelancer'), (b'Standard Business', b'Standard Business'), (b'Premier Business', b'Premier Business'), (b'Nonprofit', b'Nonprofit')]),
        ),
    ]
