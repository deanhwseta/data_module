# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setmis', '0005_auto_20180130_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='setmis.Employer'),
            preserve_default=False,
        ),
    ]
