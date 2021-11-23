# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_client_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField(max_length=10, default=0)),
                ('date_create', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 19, 17, 47, 46, 581211, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(verbose_name='Цена', max_length=10, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='shop.OrderItem'),
        ),
    ]
