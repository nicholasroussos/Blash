# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-13 17:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20161013_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 13, 17, 5, 2, 85468, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='event_description',
            field=models.TextField(default='Enter text here'),
        ),
        migrations.AlterField(
            model_name='events',
            name='new_event',
            field=models.CharField(default='Enter event title here...', max_length=140),
        ),
    ]