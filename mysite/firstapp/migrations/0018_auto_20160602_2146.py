# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_ttt'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ttt',
        ),
        migrations.AddField(
            model_name='urll',
            name='ko',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
