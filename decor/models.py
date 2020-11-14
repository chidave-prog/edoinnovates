from django.db import models


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
    button_caption=models.CharField(max_length=10)
    slider_button_animation_gesture = models.CharField(max_length=100,choices=GESTURE)
    
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.select_page} Page Slider"
