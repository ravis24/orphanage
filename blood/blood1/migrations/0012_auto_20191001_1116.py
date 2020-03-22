# Generated by Django 2.2.2 on 2019-10-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood1', '0011_remove_register1_blood_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register12',
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
            name='Register1',
        ),
    ]
