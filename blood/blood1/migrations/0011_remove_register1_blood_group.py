# Generated by Django 2.2.2 on 2019-10-01 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood1', '0010_auto_20190315_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register1',
            name='blood_group',
        ),
    ]