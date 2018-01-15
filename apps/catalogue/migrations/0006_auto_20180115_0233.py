# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20180115_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_until',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha de fin de Vigencia'),
        ),
    ]
