# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20150915_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subpage',
            old_name='subpage',
            new_name='flatpage',
        ),
    ]
