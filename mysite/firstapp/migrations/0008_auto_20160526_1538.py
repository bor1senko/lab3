# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20160520_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='add_name',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='item',
        ),
        migrations.AddField(
            model_name='author',
            name='kot',
            field=models.CharField(default=b'lol', max_length=2, choices=[(b'lol', b'1111'), (b'kotia', b'2222'), (b'petia', b'3333')]),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
