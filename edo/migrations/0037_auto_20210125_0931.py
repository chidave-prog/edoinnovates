# Generated by Django 2.2 on 2021-01-25 08:31

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0036_auto_20210122_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='hall',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='NOTE: word limit of 200 for the overview'),
        ),
        migrations.AlterField(
            model_name='programme',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='NOTE: word limit of 200 for the overview'),
        ),
        migrations.AlterField(
            model_name='startupsdandhubs',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='NOTE: word limit of 200 for the overview'),
        ),
    ]