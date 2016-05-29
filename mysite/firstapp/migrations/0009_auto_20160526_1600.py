# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_auto_20160526_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urll',
            name='add_name',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
