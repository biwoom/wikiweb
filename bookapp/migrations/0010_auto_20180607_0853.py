# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-06 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0009_publication_bw_book_cloud_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication_bw',
            name='stock_num',
            field=models.CharField(blank=True, default=1, max_length=300, null=True, verbose_name='배송료'),
        ),
    ]
