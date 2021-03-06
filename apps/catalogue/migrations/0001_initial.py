# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 00:26
from __future__ import unicode_literals

import apps.catalogue.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Está activo?')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Está activo?')),
                ('title', models.CharField(max_length=30, verbose_name='Titulo')),
                ('description', models.TextField(blank=True, max_length=60, verbose_name='Descripcion')),
                ('date_expiry', models.DateTimeField(validators=[apps.catalogue.validators.date_validator], verbose_name='Fecha de Expiracion')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'verbose_name': 'Cupon',
                'verbose_name_plural': 'Cupones',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Está activo?')),
                ('title', models.CharField(max_length=30, verbose_name='Titulo')),
                ('description', models.TextField(blank=True, max_length=60, verbose_name='Descripcion')),
                ('date_expiry', models.DateTimeField(validators=[apps.catalogue.validators.date_validator], verbose_name='Fecha de Expiracion')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Está activo?')),
                ('title', models.CharField(max_length=30, verbose_name='Titulo')),
                ('description', models.TextField(blank=True, max_length=60, verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to='products', verbose_name='Imagen')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogue.Category', verbose_name='Categoria')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
