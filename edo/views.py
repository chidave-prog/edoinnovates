from django.shortcuts import render
from .models import (Contact,
                    Programme,
                    Application,
                    Gallery,
                    Team,
                    Testimony,
                    Newsletter
                    )


def Home(request):     
    context={
        'title_tag'  : "EDO INNOVATE| Touching Lives",
        'programme': Programme.objects.all().order_by('created_at'),
        'gallery': Gallery.objects.all().order_by('created_at'),
        'testimony': Testimony.objects.all().order_by('created_at'),
        'team': Team.objects.all().order_by('created_at'),
    }
    return render(request, 'pages/index.html', context)



def AwsRestartBenin(request):     
    context={
        'title_tag'  : "EDO INNOVATE| AWS Re/Start Benin",
        'programme': Programme.objects.all().order_by('created_at'),
        'gallery': Gallery.objects.all().order_by('created_at'),
        'testimony': Testimony.objects.all().order_by('created_at'),
        'team': Team.objects.all().order_by('created_at'),
    }
    return render(request, 'pages/aws.html', context)

