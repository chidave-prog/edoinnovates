from django.db import models
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



class Contact(models.Model):
    full_names = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(
        help_text='subject', max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)

OPT_TYPE = [
    ('TRAINING', 'TRAINING'),
    ('COMPETITION', 'COMPETITION'),
    ('SCHOLARSHIP', 'SCHOLARSHIP'),   
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


class Programme(models.Model):
    programme_type = models.CharField(max_length=20,
                            choices=OPT_TYPE,                            
                            help_text='select programme type')
    title = models.CharField(max_length=200)
    description = models.TextField()
    sponsor_or_partner_logo = models.ImageField(upload_to='sponsor_or_partner')
    programme_banner = models.ImageField(upload_to='programme_banner')
    date_from = models.DateField()
    date_to = models.DateField()
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
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.title}"


class Team(models.Model):
    full_names = models.CharField(max_length=150)
    position = models.CharField(max_length=50)
    email = models.EmailField()    
    picture = models.ImageField(upload_to='team_picture')
    phone_number = models.IntegerField(help_text='phone number')   
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

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
    phone_number = models.IntegerField(help_text='phone number')
    programme_benefited_from = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField(blank=True, null=True)
    testimony = models.TextField()
    add_a_photo = models.ImageField(
        upload_to='Testimony_image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.full_names}"