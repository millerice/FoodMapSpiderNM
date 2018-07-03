# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0008_food_evaluate'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_toal_information',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=300)),
                ('shop_name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=30)),
                ('sale', models.CharField(max_length=50)),
                ('evaluate_num', models.CharField(max_length=50)),
                ('evaluate', models.CharField(max_length=50)),
            ],
        ),
    ]
