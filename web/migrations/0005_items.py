# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0004_delete_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('interval', models.IntegerField()),
                ('mailInterval', models.IntegerField()),
                ('smsInterval', models.IntegerField()),
                ('smsBegin', models.TimeField()),
                ('smsEnd', models.TimeField()),
                ('retryTimes', models.IntegerField()),
                ('describe', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('timeout', models.IntegerField()),
                ('retryInterval', models.IntegerField()),
                ('contacts', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('statusCode', models.IntegerField()),
            ],
        ),
    ]
