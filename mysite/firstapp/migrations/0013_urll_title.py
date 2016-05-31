# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_auto_20160529_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='urll',
            name='title',
            field=models.CharField(default=1, max_length=200, editable=False),
            preserve_default=False,
        ),
    ]
