# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_ttt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ttt',
            old_name='url',
            new_name='urll',
        ),
    ]
