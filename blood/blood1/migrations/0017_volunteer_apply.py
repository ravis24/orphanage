# Generated by Django 2.2.2 on 2019-10-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood1', '0016_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='volunteer_apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('emailid', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('Pin_code', models.IntegerField(max_length=30)),
                ('profile_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
