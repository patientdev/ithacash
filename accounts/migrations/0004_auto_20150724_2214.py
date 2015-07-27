# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150723_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ithacashaccount',
            old_name='address_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='ithacashaccount',
            old_name='name_business',
            new_name='entity_name',
        ),
        migrations.RenameField(
            model_name='ithacashaccount',
            old_name='address_state',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='ithacashaccount',
            old_name='address_zip_code',
            new_name='zip_code',
        ),
        migrations.RemoveField(
            model_name='ithacashaccount',
            name='name_contact',
        ),
        migrations.AddField(
            model_name='ithacashuser',
            name='full_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='account_type',
            field=models.CharField(max_length=20, choices=[(None, b'Select Account Type'), (b'Individual', b'Individual'), (b'Freelancer', b'Freelancer'), (b'Standard Business', b'Standard Business'), (b'Premium Business', b'Premium Business'), (b'Nonprofit', b'Nonprofit')]),
        ),
        migrations.AlterField(
            model_name='ithacashuser',
            name='username',
            field=models.CharField(help_text=b'Other Ithacash users can use this username to pay you.', unique=True, max_length=120),
        ),
    ]
