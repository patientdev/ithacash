# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150724_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='ithacashaccount',
            name='contact_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
