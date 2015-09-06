# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignUpPayment',
            fields=[
                ('payment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='payments.Payment')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('txn_id', models.CharField(max_length=255)),
            ],
            bases=('payments.payment',),
        ),
        migrations.AddField(
            model_name='payment',
            name='account',
            field=models.ForeignKey(related_name='payments', to='accounts.IthacashAccount'),
        ),
    ]
