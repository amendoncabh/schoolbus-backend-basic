# Generated by Django 2.1.7 on 2019-12-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20191211_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroutewithlocation',
            name='delay_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
