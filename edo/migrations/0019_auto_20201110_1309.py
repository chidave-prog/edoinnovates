# Generated by Django 2.2 on 2020-11-10 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0018_auto_20201110_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='link_to_your_whatsapp_number',
            new_name='whatsapp_number',
        ),
    ]