# Generated by Django 2.1.7 on 2019-12-17 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20191216_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='number',
        ),
    ]
