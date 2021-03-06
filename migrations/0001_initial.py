# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-13 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_announcement', models.TextField(default='Enter text here...')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_event', models.TextField(default='Enter text here...')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('student_email', models.EmailField(blank='True', default='', max_length=120)),
                ('belt_ranking', models.CharField(choices=[('W', 'White'), ('Y', 'Yellow'), ('G', 'Green'), ('Br', 'Brown'), ('Pr', 'Purple'), ('R', 'Red'), ('Bk', 'Black'), ('Bl', 'Blue')], default='W', max_length=120)),
                ('wavier_signed', models.BooleanField()),
            ],
        ),
    ]
