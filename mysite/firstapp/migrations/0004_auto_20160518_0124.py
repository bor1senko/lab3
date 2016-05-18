# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='url',
        ),
        migrations.AlterField(
            model_name='urll',
            name='add_name',
            field=models.ForeignKey(to='firstapp.Author'),
        ),
    ]
