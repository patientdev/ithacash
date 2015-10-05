# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20150929_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfiles',
            name='title',
            field=models.CharField(default='blah', unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
