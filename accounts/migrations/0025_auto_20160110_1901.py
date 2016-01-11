# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_ithacashaccount_registration_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='website',
            field=models.URLField(default=b'', max_length=255, blank=True),
        ),
    ]
