# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_form_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('atitle', models.CharField(verbose_name='名称', max_length=30)),
                ('aParent', models.ForeignKey(to='foodapp.AreaInfo', null=True, blank=True, verbose_name='父级名称')),
            ],
        ),
        migrations.DeleteModel(
            name='form_table',
        ),
        migrations.RemoveField(
            model_name='food_table',
            name='food_name',
        ),
        migrations.RemoveField(
            model_name='food_table',
            name='food_num',
        ),
    ]
