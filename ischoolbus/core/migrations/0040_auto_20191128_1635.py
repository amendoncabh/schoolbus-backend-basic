# Generated by Django 2.2.4 on 2019-11-28 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20191128_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='reason_for_absence_missing',
            new_name='reason_for_absence_or_missing',
        ),
    ]
