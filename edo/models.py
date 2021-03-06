from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import os
from io import BytesIO


def edit_photo(photo, width, height):
    if photo:
        imageTemproary = Image.open(photo)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize((width, height))
        try:
            imageTemproaryResized.save(
                outputIoStream, format="JPEG", quality=80)
        except:
            imageTemproaryResized.save(
                outputIoStream, format="PNG", quality=80)
            try:
                imageTemproaryResized.save(
                    outputIoStream, format="GIF", quality=80
                )
            except:
                imageTemproaryResized.save(
                    outputIoStream, format="BMP", quality=80
                )
        outputIoStream.seek(0)
        photo = InMemoryUploadedFile(
            outputIoStream,
            "ImageField",
            "%s.jpg" % photo.name.split(".")[0],
            "profile_photo/jpeg",
            sys.getsizeof(outputIoStream),
            None,
        )
    else:
        photo = None
    return photo


OPT_TYPE = [
    ('TRAINING', 'TRAINING'),
    ('COMPETITION', 'COMPETITION'),
    ('SCHOLARSHIP', 'SCHOLARSHIP'),
    ('OPPORTUNITY', 'OPPORTUNITY'),
]
GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),

]
PHOTO_TYPE = [
    ('Gallery', 'Gallery'),
    ('HUB', 'HUB'),
    ('StartUps', 'StartUps'),
    ('halls', 'halls'),
]
TEAM_CATEGORY = [
    ('aws_instructors', 'aws_instructors'),
    ('Borad_members', 'Borad_members'),
    ('others', 'others'),
]
StartupsdAndHubs_Choices = [
    ('start_up', 'start_up'),
    ('hub', 'hub'),
]


class Contact(models.Model):
    full_names = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(
        help_text='subject', max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class PostView(models.Model):
    visited = models.CharField(max_length=200, blank=True, null=True)
    blog = models.ForeignKey(
        'Blog', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.visited)

    def save(self, *args, **kwargs):
        if self.quote:
            self.visited = self.quote
        super(PostView, self).save(*args, **kwargs)


class Comment(models.Model):
    full_names = models.CharField(max_length=200)
    phone_number = models.CharField(help_text='phone number', max_length=20)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    blog = models.ForeignKey(
        'Blog', related_name='blog_comment', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    reply = models.TextField(blank=True, null=True)
    replyed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.full_names) + ' commented on ' + str(self.blog)


class Blog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    caption_picture = models.ImageField(
        upload_to='blog', blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    connect = models.CharField(max_length=200, blank=True, null=True)
    author_photo = models.ImageField(
        upload_to='news author photo', blank=True, null=True)
    views = models.CharField(max_length=20, default=0, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        edit_photo(self.caption_picture, 400, 400)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    @property
    def get_comments(self):
        return self.blog_comment.all().order_by('-created_at')

    @property
    def total_comments(self):
        return Comment.objects.filter(blog=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(blog=self).count()


class Programme(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField(
        help_text='NOTE: word limit of 200 for the overview')
    programme_banner = models.ImageField(upload_to='programme_banner')
    application_link = models.URLField(
        help_text="link to google form or any other application link", blank=True, null=True)
    publish = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True,
                            help_text="please leave this field blank")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('programme', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        edit_photo(self.programme_banner, 50, 50)
        self.slug = slugify(str(self.title))
        super(Programme, self).save(*args, **kwargs)


class Application(models.Model):
    programme = models.ForeignKey(
        'Programme', null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=GENDER)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, help_text='phone number')
    address = models.TextField()
    aproved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.programme)


class StartupsdAndHubs(models.Model):
    category = models.CharField(
        null=True, max_length=10, choices=StartupsdAndHubs_Choices)
    name = models.CharField(max_length=200)
    about = RichTextUploadingField(
        help_text='NOTE: word limit of 200 for the overview')
    logo = models.ImageField(upload_to='programme_banner')
    phone_number = models.CharField(
        max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    Instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True,
                            help_text="please leave this field blank")
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('startupsdsndhub', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        edit_photo(self.logo, 300, 300)
        self.slug = slugify(str(self.name))
        super(StartupsdAndHubs, self).save(*args, **kwargs)


class Hall(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextUploadingField(
        help_text='NOTE: word limit of 200 for the overview')
    photo = models.ImageField(upload_to='Photo_Gallery')
    photo_2 = models.ImageField(
        upload_to='Photo_Gallery', blank=True, null=True)
    photo_3 = models.ImageField(
        upload_to='Photo_Gallery', blank=True, null=True)
    publish = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True,
                            help_text="please leave this field blank")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('hall', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        edit_photo(self.photo, 300, 300)
        if self.photo_2:
            edit_photo(self.photo_2, 300, 300)
        if self.photo_3:
            edit_photo(self.photo_3, 300, 300)
        self.slug = slugify(str(self.name))
        super(Hall, self).save(*args, **kwargs)


class Gallery(models.Model):
    photo_type = models.CharField(max_length=20, choices=PHOTO_TYPE)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    photo = models.ImageField(upload_to='Photo_Gallery')
    photo_2 = models.ImageField(
        upload_to='Photo_Gallery', blank=True, null=True)
    photo_3 = models.ImageField(
        upload_to='Photo_Gallery', blank=True, null=True)
    start_up_phone_number = models.CharField(
        max_length=20, blank=True, null=True)
    start_up_email = models.EmailField(blank=True, null=True)
    start_up_website_link = models.URLField(blank=True, null=True)
    start_up_facebook_link = models.URLField(blank=True, null=True)
    start_up_twitter_link = models.URLField(blank=True, null=True)
    start_up_Instagram_link = models.URLField(blank=True, null=True)
    start_up_linkedin_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        edit_photo(self.photo, 300, 300)
        edit_photo(self.photo_2, 300, 300)
        edit_photo(self.photo_3, 300, 300)
        self.slug = slugify(str(self.title))
        super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('gallery-detail', kwargs={'slug': self.slug})


class Team(models.Model):
    office = models.CharField(max_length=20, choices=TEAM_CATEGORY)
    full_names = models.CharField(max_length=150)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    picture = models.ImageField(upload_to='team_picture')
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True, default='+123',
                                       help_text='phone number in International formart without the plus e.g (2348012345...)')
    link_to_your_linkedin_account = models.URLField(blank=True, null=True)
    link_to_your_twitter_account = models.URLField(blank=True, null=True)
    # facebook = models.URLField(blank=True, null=True)
    # instagram = models.URLField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.full_names)

    def save(self, *args, **kwargs):
        edit_photo(self.picture, 200, 200)
        if self.whatsapp_number:
            self.whatsapp_number = str(self.whatsapp_number).replace('+', '')
        super(Team, self).save(*args, **kwargs)


class Newsletter(models.Model):
    sub_email = models.EmailField(blank=True, null=True)
    subscribe = models.BooleanField(default=True)

    def __str__(self):
        return self.sub_email


class Testimony(models.Model):
    full_names = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    programme_benefited_from = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    testimony = models.TextField(max_length=800, help_text="word limit of 800")
    add_a_photo = models.ImageField(
        upload_to='Testimony_image', blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.full_names)
