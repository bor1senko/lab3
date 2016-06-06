# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0019_auto_20160602_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='urll',
            name='flag',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
