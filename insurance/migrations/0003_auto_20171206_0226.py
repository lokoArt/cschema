# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-06 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20171205_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnumOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'insurance_enum_option',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('number', 'number'), ('text', 'text'), ('date', 'date'), ('enum', 'enum')], max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='schema',
            name='schema',
        ),
        migrations.AddField(
            model_name='field',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='insurance.Schema'),
        ),
        migrations.AddField(
            model_name='enumoption',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='insurance.Field'),
        ),
    ]
