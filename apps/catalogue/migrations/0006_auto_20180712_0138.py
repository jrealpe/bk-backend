# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 01:38
from __future__ import unicode_literals

import apps.catalogue.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20180708_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='categories', validators=[apps.catalogue.validators.image_validator], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, validators=[apps.catalogue.validators.title_validator]),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='image',
            field=models.ImageField(upload_to='', validators=[apps.catalogue.validators.image_validator], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='title',
            field=models.CharField(max_length=30, validators=[apps.catalogue.validators.title_validator], verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(upload_to='', validators=[apps.catalogue.validators.image_validator], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=30, validators=[apps.catalogue.validators.title_validator], verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=150, validators=[apps.catalogue.validators.description_validator, django.core.validators.MaxLengthValidator(150)], verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products', validators=[apps.catalogue.validators.image_validator], verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=30, validators=[apps.catalogue.validators.title_validator], verbose_name='Titulo'),
        ),
    ]
