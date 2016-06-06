# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0018_auto_20160602_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urll',
            name='ko',
        ),
        migrations.AddField(
            model_name='text',
            name='flag',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
