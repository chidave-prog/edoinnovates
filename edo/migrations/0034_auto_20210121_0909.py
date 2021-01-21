# Generated by Django 2.2 on 2021-01-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edo', '0033_programme_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='halls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(help_text='NOTE: word limit of 700', max_length=700)),
                ('photo', models.ImageField(upload_to='Photo_Gallery')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='Photo_Gallery')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='Photo_Gallery')),
                ('publish', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, help_text='please leave this field blank', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StartupsdAndHubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField(help_text='NOTE: word limit of 700', max_length=700)),
                ('logo', models.ImageField(upload_to='programme_banner')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('Instagram_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, help_text='please leave this field blank', null=True)),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='programme',
            name='link_to_program',
        ),
        migrations.RemoveField(
            model_name='programme',
            name='programme_type',
        ),
        migrations.AlterField(
            model_name='programme',
            name='slug',
            field=models.SlugField(blank=True, help_text='please leave this field blank', null=True),
        ),
    ]
