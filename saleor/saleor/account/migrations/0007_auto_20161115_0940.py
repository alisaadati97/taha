# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-15 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("account", "0006_auto_20160829_0819")]

    replaces = [("userprofile", "0007_auto_20161115_0940")]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=256, verbose_name="given name"
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=256, verbose_name="family name"
            ),
        ),
    ]
