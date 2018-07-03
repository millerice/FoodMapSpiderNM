# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_auto_20180524_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('atitle', models.CharField(max_length=30, verbose_name='名称')),
                ('aParent', models.ForeignKey(null=True, verbose_name='父级名称', blank=True, to='foodapp.AreaInfo')),
            ],
        ),
    ]
