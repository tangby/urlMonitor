# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='items',
        ),
    ]