# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_uploadedfiles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='subpage',
            name='meta_image',
            field=models.TextField(default=b'https://ithacash.com/static/img/ithacash_logo_rgb_325x124.png', blank=True),
        ),
    ]
