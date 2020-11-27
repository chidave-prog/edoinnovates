# Generated by Django 2.2 on 2020-11-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0028_gallery_start_up_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.CharField(help_text='phone number', max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='start_up_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='whatsapp_number',
            field=models.CharField(default='+123', help_text='phone number in International formart without the plus e.g (2348012345...)', max_length=20),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]