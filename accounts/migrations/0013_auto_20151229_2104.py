# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20151222_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='tin',
            field=encrypted_fields.fields.EncryptedCharField(max_length=255, null=True),
        ),
    ]
