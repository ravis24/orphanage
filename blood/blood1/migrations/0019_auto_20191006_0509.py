# Generated by Django 2.2.2 on 2019-10-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood1', '0018_auto_20191005_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_apply',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
