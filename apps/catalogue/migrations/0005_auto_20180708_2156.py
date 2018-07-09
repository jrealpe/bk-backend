# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-08 21:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20180707_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Ingrese solo letras', 'invalid_username')]),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Ingrese solo letras', 'invalid_username')], verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Ingrese solo letras', 'invalid_username')], verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=150, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9 ]+$', 'Ingrese solo letras y números', 'invalid_username')], verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Ingrese solo letras', 'invalid_username')], verbose_name='Titulo'),
        ),
    ]