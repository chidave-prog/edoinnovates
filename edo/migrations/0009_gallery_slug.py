# Generated by Django 2.2 on 2020-11-06 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0008_team_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]