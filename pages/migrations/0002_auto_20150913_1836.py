# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ithacashsubpages',
            name='id',
        ),
        migrations.AlterField(
            model_name='ithacashsubpages',
            name='subpage',
            field=models.OneToOneField(primary_key=True, serialize=False, to='flatpages.FlatPage'),
        ),
    ]
