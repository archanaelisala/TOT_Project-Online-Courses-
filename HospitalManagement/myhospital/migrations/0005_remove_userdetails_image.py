# Generated by Django 3.1.4 on 2021-01-04 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhospital', '0004_userdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='Image',
        ),
    ]
