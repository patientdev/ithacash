# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_ithacashaccount_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ithacashaccount',
            name='billing_frequency',
            field=models.CharField(default=b'Monthly', max_length=11, choices=[(b'Monthly', b'Monthly'), (b'Semi-Annual', b'Semi-Annual')]),
        ),
    ]
