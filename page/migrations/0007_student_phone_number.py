# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-03 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_faqmod'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(default='0'),
        ),
    ]
