# Generated by Django 2.2 on 2020-11-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0026_auto_20201126_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='start_up_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
