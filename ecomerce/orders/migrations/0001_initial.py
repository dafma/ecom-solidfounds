# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=250)),
                ('codigo_postal', models.CharField(max_length=7)),
                ('ciudad', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('pagado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-creado',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Orden')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Producto')),
            ],
        ),
    ]
