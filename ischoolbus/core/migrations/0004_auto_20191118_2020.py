# Generated by Django 2.2.3 on 2019-11-18 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191118_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='first_name',
            new_name='id_number',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='district',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='home_number',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='province',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='ward',
        ),
    ]
