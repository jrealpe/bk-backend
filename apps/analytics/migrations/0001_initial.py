# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 15:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0008_auto_20180811_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_views', models.PositiveIntegerField(default=0, verbose_name='Visualizaciones')),
                ('coupon', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='stats', to='catalogue.Coupon', verbose_name='Cupón')),
            ],
            options={
                'verbose_name': 'Historial de Cupón',
                'verbose_name_plural': 'Historial de Cupones',
                'ordering': ['-num_views'],
            },
        ),
        migrations.CreateModel(
            name='OfferRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_views', models.PositiveIntegerField(default=0, verbose_name='Visualizaciones')),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='stats', to='catalogue.Offer', verbose_name='Oferta')),
            ],
            options={
                'verbose_name': 'Historial de Oferta',
                'verbose_name_plural': 'Historial de Ofertas',
                'ordering': ['-num_views'],
            },
        ),
        migrations.CreateModel(
            name='ProductRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_views', models.PositiveIntegerField(default=0, verbose_name='Visualizaciones')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='stats', to='catalogue.Product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Historial de Producto',
                'verbose_name_plural': 'Historial de Productos',
                'ordering': ['-num_views'],
            },
        ),
        migrations.CreateModel(
            name='UserCouponView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Coupon', verbose_name='Cupón')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Visualización de Usuario-Cupón',
                'verbose_name_plural': 'Visualizaciones de Usuario-Cupón',
            },
        ),
        migrations.CreateModel(
            name='UserOfferView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Offer', verbose_name='Oferta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Visualización de Usuario-Oferta',
                'verbose_name_plural': 'Visualizaciones de Usuario-Oferta',
            },
        ),
        migrations.CreateModel(
            name='UserProductView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product', verbose_name='Producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Visualización de Usuario-Producto',
                'verbose_name_plural': 'Visualizaciones de Usuario-Producto',
            },
        ),
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_product_views', models.PositiveIntegerField(default=0, verbose_name='Vistas de Producto')),
                ('num_coupon_views', models.PositiveIntegerField(default=0, verbose_name='Vistas de Cupones')),
                ('num_offer_views', models.PositiveIntegerField(default=0, verbose_name='Vistas de Ofertas')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Historial de Usuario',
                'verbose_name_plural': 'Historial de Usuarios',
            },
        ),
    ]
