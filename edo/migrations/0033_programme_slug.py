# Generated by Django 2.2 on 2021-01-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0032_auto_20201204_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]