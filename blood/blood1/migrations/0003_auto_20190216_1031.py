# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-16 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood1', '0002_auto_20190216_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='blood_group',
            new_name='bloodgroup',
        ),
    ]