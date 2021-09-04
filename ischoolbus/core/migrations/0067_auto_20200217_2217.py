# Generated by Django 2.1.7 on 2020-02-17 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20200217_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='student',
        ),
        migrations.AddField(
            model_name='contact',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='core.Parent'),
        ),
    ]
