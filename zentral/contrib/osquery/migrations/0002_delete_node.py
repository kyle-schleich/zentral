# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osquery', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Node',
        ),
    ]
