# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_auto_20180524_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areainfo',
            name='aParent',
        ),
        migrations.DeleteModel(
            name='AreaInfo',
        ),
    ]
