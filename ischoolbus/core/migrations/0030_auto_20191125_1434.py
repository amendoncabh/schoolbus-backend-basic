# Generated by Django 2.2.1 on 2019-11-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_buslocation_polygon_to_next_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buslocation',
            name='polygon_to_next_location',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='buslocation',
            name='ward',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
