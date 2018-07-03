# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_data', models.DateField()),
                ('province_name', models.CharField(max_length=60)),
                ('tian_num', models.IntegerField(default=0)),
                ('huo_num', models.IntegerField(default=0)),
                ('xiao_num', models.IntegerField(default=0)),
                ('xi_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='food_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_data', models.DateField()),
                ('province_name', models.CharField(max_length=60)),
                ('food_name', models.CharField(max_length=60)),
                ('food_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='food_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('time_data', models.DateField()),
                ('food_name', models.CharField(max_length=60)),
                ('food_num_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='heroinfo',
            name='hbook',
        ),
        migrations.DeleteModel(
            name='BookInfo',
        ),
        migrations.DeleteModel(
            name='HeroInfo',
        ),
    ]
