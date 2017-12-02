# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-30 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0006_dict_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='dict',
            name='bu_classification',
            field=models.CharField(choices=[('《경장》', '《경장》'), ('《율장》', '《율장》'), ('《논장》', '《논장》'), ('《주석》', '《주석》'), ('《찬가》', '《찬가》'), ('《서신》', '《서신》'), ('《시문》', '《시문》'), ('《역사》', '《역사》'), ('《우화》', '《우화》'), ('《인명》', '《인명》'), ('《지명》', '《지명》'), ('《의례》', '《의례》'), ('《복식》', '《복식》'), ('《사원》', '《사원》')], default='FR', max_length=10),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_antonym',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_classical_chinese_entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_english_entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_future_tense',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_honorific',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_humble_terms',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_imperative',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_korean_entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_pali_entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_past_tense',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_present_tense',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_sanskrit_entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_synonym',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_thesaurus',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dict',
            name='ti_wylie',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
