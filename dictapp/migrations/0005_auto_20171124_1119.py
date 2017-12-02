# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-24 02:19
from __future__ import unicode_literals

import dictapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0004_auto_20171124_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='dict',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=dictapp.models.upload_path_file),
        ),
        migrations.AlterField(
            model_name='dict',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=dictapp.models.upload_path_img, width_field='width_field'),
        ),
    ]
