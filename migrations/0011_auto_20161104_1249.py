# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_auto_20161104_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='class_choices',
            new_name='class_choice',
        ),
    ]
