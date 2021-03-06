# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('keyword', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='article')),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_alis', models.CharField(max_length=20)),
                ('father_node', models.IntegerField()),
                ('keyword', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'banner',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='father_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backblog.Banner'),
        ),
    ]
