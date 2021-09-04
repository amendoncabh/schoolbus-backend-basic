# Generated by Django 2.2.4 on 2019-11-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20191125_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bussupervisor',
            name='avatar',
            field=models.FileField(upload_to='supervisors'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='drivers'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='avatar',
            field=models.FileField(upload_to='parents'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='students'),
        ),
    ]