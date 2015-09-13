# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20150913_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashsubpages',
            name='subpage',
            field=models.OneToOneField(related_name='subpage', primary_key=True, serialize=False, to='flatpages.FlatPage'),
        ),
    ]
