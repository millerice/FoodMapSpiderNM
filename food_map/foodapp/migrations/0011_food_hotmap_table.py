# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0010_auto_20180529_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_hotmap_table',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('food_num', models.CharField(max_length=50)),
            ],
        ),
    ]
