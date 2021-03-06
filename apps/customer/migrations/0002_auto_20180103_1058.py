# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-03 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.City', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='user',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.Province', verbose_name='Provincia'),
        ),
    ]
