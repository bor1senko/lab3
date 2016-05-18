# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_adres', models.URLField()),
                ('add_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='URL',
        ),
    ]
