# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-08 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0003_auto_20171107_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otaenrollment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='otaenrollment',
            name='name',
            field=models.CharField(default='UNKNOWN', max_length=256, unique=True),
            preserve_default=False,
        ),
    ]
