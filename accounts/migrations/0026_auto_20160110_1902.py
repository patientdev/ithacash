# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20160110_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='website',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
