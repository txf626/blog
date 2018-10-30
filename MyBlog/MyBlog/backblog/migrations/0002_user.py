# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('new_password', models.CharField(max_length=100)),
                ('old_password', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]