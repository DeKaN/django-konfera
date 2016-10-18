# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konfera', '0003_auto_20161012_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='Slug field, relative URL to the event.', max_length=128, unique=True, verbose_name='Event url'),
        ),
    ]