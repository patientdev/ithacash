# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20151218_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='is_ssn',
            field=models.NullBooleanField(),
        ),
    ]
