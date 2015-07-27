# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150723_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ithacashaccount',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ithacashaccount',
            name='name_login',
        ),
        migrations.AddField(
            model_name='ithacashaccount',
            name='owner',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ithacashuser',
            name='created',
            field=models.DateTimeField(default=None, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ithacashaccount',
            name='account_type',
            field=models.CharField(max_length=20, choices=[(None, b'Select Account Type'), (b'Individual', b'Individual'), (b'Freelancer', b'Freelancer'), (b'Business', b'Business'), (b'Nonprofit', b'Nonprofit')]),
        ),
    ]
