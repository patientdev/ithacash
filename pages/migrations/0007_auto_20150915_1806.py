# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('pages', '0006_auto_20150913_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPage',
            fields=[
                ('subpage', models.OneToOneField(related_name='subpage', primary_key=True, serialize=False, blank=True, to='flatpages.FlatPage')),
                ('heading', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='ithacashsubpages',
            name='subpage',
        ),
        migrations.DeleteModel(
            name='IthacashSubPages',
        ),
    ]
