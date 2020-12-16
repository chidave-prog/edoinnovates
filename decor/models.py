from django.db import models
from django.urls import reverse
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
                outputIoStream, format="JPEG", quality=100)
        except:
            imageTemproaryResized.save(
                outputIoStream, format="PNG", quality=100)
            try:
                imageTemproaryResized.save(
                    outputIoStream, format="GIF", quality=100
                )
            except:
                imageTemproaryResized.save(
                    outputIoStream, format="BMP", quality=100
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

PAGES=[
     ('home', 'home'),
      ('aws_page', 'aws_page'),
]
GESTURE=[
    ('fadeInUp', 'fadeInUp'),
     ('zoomIn', 'zoomIn'),
     ('fadeInDown', 'fadeInDown'),
     ('fadeInLeft', 'fadeInLeft'),
     ('fadeInRight', 'fadeInRight'),
     ('slideInDown', 'slideInDown'),
      ('slideInLeft', 'slideInLeft'),
       ('slideInRight', 'slideInRight'),
       ('slideInUp', 'slideInUp'),
       ('bounceInDown', 'bounceInDown'),
       ('bounceInLeft', 'bounceInLeft'),
       ('bounceInRight', 'bounceInRight'),
       ('bounceInUp', 'bounceInUp'),
       ('lightSpeedIn', 'lightSpeedIn'),
       ('lightSpeedOut', 'lightSpeedOut'),
       ('flipInY', 'flipInY'),
        ('flipInX', 'flipInX'),
]

class Pageslider(models.Model):
    select_page = models.CharField(max_length=100,choices=PAGES)
    slide_image = models.ImageField(upload_to='slide_images')
    caption_top_title_small = models.CharField(max_length=100, blank=True, null=True)      
    caption_mid_title_large = models.CharField(max_length=100)
    top_slider_animation_gesture = models.CharField(max_length=100,choices=GESTURE)
    caption_buttom_title_small = models.CharField(max_length=100, blank=True, null=True)
    bottom_slider_animation_gesture = models.CharField(max_length=100,choices=GESTURE)
    button_caption=models.CharField(max_length=20)
    slider_button_animation_gesture = models.CharField(max_length=100,choices=GESTURE)
    
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.select_page} Page Slider"

    def save(self, *args, **kwargs):        
        edit_photo(self.slide_image, 300, 300)
        super(Pageslider, self).save(*args, **kwargs)
        
