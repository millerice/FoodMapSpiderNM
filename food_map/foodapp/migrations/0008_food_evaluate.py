# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0007_areainfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_evaluate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluate', models.CharField(max_length=50)),
            ],
        ),
    ]
