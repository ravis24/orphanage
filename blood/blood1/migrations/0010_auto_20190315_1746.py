# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-15 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood1', '0009_remove_register_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=8)),
                ('blood_group', models.CharField(choices=[('a', 'a+'), ('b', 'a-'), ('c', 'o+'), ('d', 'o-'), ('e', 'b+')], max_length=128)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
