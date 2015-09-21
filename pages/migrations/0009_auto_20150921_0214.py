# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20150915_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='subpage',
            name='meta_desc',
            field=models.TextField(default=b"Ithacash is a regional benefit currency for Ithaca and Tompkins County. Every Ithaca Dollar spent becomes an immediate buy-local success. There's no catch. It's money that stays in our region by design, strengthening our local economy and meeting our community's needs, period.", blank=True),
        ),
        migrations.AddField(
            model_name='subpage',
            name='meta_keywords',
            field=models.TextField(default=b'ithaca, local, currency', blank=True),
        ),
    ]
