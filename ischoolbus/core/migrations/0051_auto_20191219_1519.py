# Generated by Django 2.1.7 on 2019-12-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_remove_bus_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]