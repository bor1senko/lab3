# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_urll_html_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urll',
            old_name='html_text',
            new_name='index',
        ),
    ]
