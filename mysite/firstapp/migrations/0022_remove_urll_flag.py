# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_urll_hight_recurcian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urll',
            name='flag',
        ),
    ]