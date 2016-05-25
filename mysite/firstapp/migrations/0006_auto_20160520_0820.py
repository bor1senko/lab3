# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='post_text',
            field=models.TextField(),
        ),
    ]
