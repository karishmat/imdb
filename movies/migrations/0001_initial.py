# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-06 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('imdb_score', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('genre', models.CharField(blank=True, max_length=200, null=True)),
                ('director', models.CharField(blank=True, max_length=200, null=True)),
                ('popularity_score', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]