# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20151229_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ithacashaccount',
            name='tin',
            field=encrypted_fields.fields.EncryptedCharField(help_text=b'This is a secure site. Your information will not be seen by anyone internally, distributed, or shared.', max_length=255, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9)]),
        ),
    ]
