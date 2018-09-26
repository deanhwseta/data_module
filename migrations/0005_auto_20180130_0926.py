# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setmis', '0004_non_nqf_intervention_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='provider_class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setmis.Provider_class_Id', to_field='lookup'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider_status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setmis.Provider_Status_Id', to_field='lookup'),
        ),
    ]