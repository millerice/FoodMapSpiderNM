# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_auto_20180420_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='nuomi_information_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('shop_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=60)),
                ('work_time', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=30)),
                ('evaluate_num', models.CharField(max_length=50)),
                ('good_level', models.CharField(max_length=50)),
                ('commonly_level', models.CharField(max_length=50)),
                ('bad_level', models.CharField(max_length=50)),
                ('evaluate', models.CharField(max_length=50)),
            ],
        ),
    ]
