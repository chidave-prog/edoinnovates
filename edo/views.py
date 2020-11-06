from django.shortcuts import render
from django.views import generic
from .models import (
                    Contact,
                    Programme,
                    PostView,
                    Comment,
                    Blog,
                    Application,
                    Gallery,
                    Team,
                    Testimony,
                    Newsletter
                    )
def newsletter(arg):
    if arg.request.POST.get("sub_email"):
        newsletter, created = Newsletter.objects.get_or_create(
            sub_email=arg.request.POST.get("sub_email"),
            subscribe=True
        )
        newsletter.save()
        return messages.info(arg.request, "SUBSCRIBED!")

def Home(request):     
    context={
        'title_tag'  : "EDO INNOVATE| Touching Lives",
        'programme': Programme.objects.filter(publish=True).order_by('-created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'gallery': Gallery.objects.filter(publish=True).order_by('-created_at'),
       
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


class GalleryDetailView(generic.DetailView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'pages/gallery.html'
    