# Generated by Django 2.2 on 2020-11-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0029_auto_20201126_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='whatsapp_number',
            field=models.CharField(blank=True, default='+123', help_text='phone number in International formart without the plus e.g (2348012345...)', max_length=20, null=True),
        ),
    ]