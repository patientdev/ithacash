# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_subpage_meta_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpage',
            name='meta_image',
            field=models.TextField(default=b'https://ithacash.com/static/img/ithacash_logo_rgb_747x200.png', blank=True),
        ),
    ]
