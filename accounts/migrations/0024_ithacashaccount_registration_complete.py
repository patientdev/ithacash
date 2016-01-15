# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20160107_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='ithacashaccount',
            name='registration_complete',
            field=models.BooleanField(default=False),
        ),
    ]
