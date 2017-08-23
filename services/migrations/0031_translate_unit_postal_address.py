# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-02 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0030_reverse_unit_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='address_postal_full_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='address_postal_full_fi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='address_postal_full_sv',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
