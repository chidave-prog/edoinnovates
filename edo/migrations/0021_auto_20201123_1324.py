# Generated by Django 2.2 on 2020-11-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0020_auto_20201110_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='photo_type',
        ),
        migrations.AddField(
            model_name='gallery',
            name='position',
            field=models.CharField(choices=[('aws_instructors', 'aws_instructors'), ('Borad_members', 'Borad_members'), ('others', 'others')], default='Board_mambers', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='photo_type',
            field=models.CharField(choices=[('Gallery', 'Gallery'), ('HUB', 'HUB'), ('Sartups', 'Sartups')], default='Board_mambers', max_length=100),
            preserve_default=False,
        ),
    ]