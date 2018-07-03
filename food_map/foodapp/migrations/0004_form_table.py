# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_nuomi_information_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_table',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('shop_name', models.CharField(max_length=200)),
                ('evaluate', models.CharField(max_length=50)),
            ],
        ),
    ]
