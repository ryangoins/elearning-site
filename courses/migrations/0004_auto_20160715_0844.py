# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150601_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='course',
        ),
        migrations.DeleteModel(
            name='Step',
        ),
    ]