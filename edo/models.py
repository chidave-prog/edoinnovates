from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.template.defaultfilters import slugify
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import os
from io import BytesIO



def edit_photo(photo):
    if photo:
        imageTemproary = Image.open(photo)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize((200, 200))
        try:
            imageTemproaryResized.save(
                outputIoStream, format="JPEG", quality=150)
        except:
            imageTemproaryResized.save(
                outputIoStream, format="PNG", quality=150)
            try:
                imageTemproaryResized.save(
                    outputIoStream, format="GIF", quality=150
                )
            except:
                imageTemproaryResized.save(
                    outputIoStream, format="BMP", quality=150
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
    ('Sartups', 'Sartups'),  
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
        return f"{self.full_names} commented on {self.blog}" 

class Blog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)   
    content = HTMLField()
    caption_picture = models.ImageField(
        upload_to='news', blank=True, null=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
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
    programme_type = models.CharField(max_length=20,
                            choices=OPT_TYPE,                            
                            help_text='select programme type')
    title = models.CharField(max_length=200)
    description = models.TextField(help_text='NOTE: word limit of 700', max_length=700)    
    programme_banner = models.ImageField(upload_to='programme_banner')
    link_to_program = models.URLField(blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.title} | {self.programme_type} | {self.date_from}  -  {self.date_to}"

class Application(models.Model):
    programme = models.ForeignKey('Programme', null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6,choices=GENDER)
    email = models.EmailField()  
    phone_number = models.IntegerField(help_text='phone number')
    address = models.TextField()
    aproved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.programme} | {self.first_name} | {self.email} |  {self.aproved}"

class Gallery(models.Model):
    photo_type = models.CharField(max_length=100,choices=PHOTO_TYPE)
    title = models.CharField(max_length=200)
    description = models.TextField()    
    photo = models.ImageField(upload_to='Photo_Gallery')
    photo_2 = models.ImageField(upload_to='Photo_Gallery',blank=True, null=True)
    photo_3 = models.ImageField(upload_to='Photo_Gallery',blank=True, null=True)
    link_address_4_start_ups = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} of  {self.photo_type}"

    def get_absolute_url(self):
        return reverse('gallery-detail', kwargs={'slug': self.slug})

class Team(models.Model):
    full_names = models.CharField(max_length=150)
    position = models.CharField(max_length=50)
    email = models.EmailField()    
    picture = models.ImageField(upload_to='team_picture')
    link_to_your_whatsapp_number = models.IntegerField(default='+123', help_text='phone number in International formart e.g (+2348012345...)')   
    link_to_your_linkedin_account = models.URLField(blank=True, null=True)    
    link_to_your_twitter_account = models.URLField(blank=True, null=True)
    # facebook = models.URLField(blank=True, null=True)
    # instagram = models.URLField(blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.full_names}"

    def save(self, *args, **kwargs):  
        edit_photo(self.picture)
        super(Team, self).save(*args, **kwargs)

class Newsletter(models.Model):
    sub_email = models.EmailField(blank=True, null=True)
    subscribe = models.BooleanField(default=True)

    def __str__(self):
        return self.sub_email

class Testimony(models.Model):
    full_names = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    programme_benefited_from =  models.ForeignKey(
        'Programme', null=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    testimony = models.TextField()
    add_a_photo = models.ImageField(
        upload_to='Testimony_image', blank=True, null=True)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.full_names}"