# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20160520_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=250, blank=True)),
                ('image', models.ImageField(upload_to=b'photos')),
                ('add_name', models.ForeignKey(to='firstapp.Author')),
                ('item', models.ForeignKey(to='firstapp.Item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.RemoveField(
            model_name='blog_post',
            name='add_name',
        ),
        migrations.DeleteModel(
            name='blog_post',
        ),
    ]
