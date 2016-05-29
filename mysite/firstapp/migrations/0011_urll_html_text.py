# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='urll',
            name='html_text',
            field=models.TextField(default=1, editable=False),
            preserve_default=False,
        ),
    ]
