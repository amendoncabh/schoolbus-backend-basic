# Generated by Django 2.2.1 on 2019-11-26 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20191125_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='buslocation',
            name='number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]