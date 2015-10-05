# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_uploadedfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfiles',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
    ]
