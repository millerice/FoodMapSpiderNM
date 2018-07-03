# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0009_food_toal_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food_type',
            name='food_num_total',
        ),
        migrations.RemoveField(
            model_name='food_type',
            name='time_data',
        ),
    ]
