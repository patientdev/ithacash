# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 18:27
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20160120_0635'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='ithacashuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
