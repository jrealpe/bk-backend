# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20180117_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Actuaizado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Actuaizado'),
        ),
    ]
