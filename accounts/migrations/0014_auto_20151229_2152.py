# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20151229_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='tin',
            field=encrypted_fields.fields.EncryptedCharField(max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9)]),
        ),
    ]
