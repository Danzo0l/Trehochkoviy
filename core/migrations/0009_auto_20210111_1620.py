# Generated by Django 3.1.4 on 2021-01-11 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201216_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talantuser',
            name='cs_process',
        ),
        migrations.RemoveField(
            model_name='talantuser',
            name='dota_process',
        ),
    ]
