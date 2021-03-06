# Generated by Django 2.2 on 2020-11-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0017_auto_20201110_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='description',
            field=models.TextField(help_text='NOTE: word limit of 700', max_length=700),
        ),
        migrations.AlterField(
            model_name='team',
            name='link_to_your_whatsapp_number',
            field=models.IntegerField(default='+123', help_text='phone number in International formart e.g (+2348012345...)'),
        ),
    ]
