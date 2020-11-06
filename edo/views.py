from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
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
def Newsletter(request):
    if request.POST.get("sub_email"):
        newsletter, created = Newsletter.objects.get_or_create(
            sub_email=request.POST.get("sub_email"),
            subscribe=True
        )
        newsletter.save()
        if request.is_ajax():       
            return JsonResponse({'form': "sucessfully subscribed!"})
    
def Search(request):
    keyword = request.POST.get("search")
    if keyword:
        context = {
                'title_tag'  : "EDO INNOVATE|" + f"{keyword}",
        }
        if request.is_ajax():
            html = render_to_string('pages/search.html',context,request=request)
            return JsonResponse({'form': html})
        
def Contact(request):
    if request.is_ajax():       
        return JsonResponse({'form': "sucessfully subscribed!"})



def Home(request):     
    context={
        'title_tag'  : "EDO INNOVATE| Touching Lives",
        'programme': Programme.objects.filter(publish=True).order_by('-created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'gallery': Gallery.objects.filter(publish=True).order_by('-created_at'),
        'blog': Blog.objects.filter(publish=True).order_by('-created_at')[:4],
        'team': Team.objects.filter(publish=True).order_by('-created_at'),
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

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 8
    context_object_name = 'news'
    template_name = 'pages/news_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = "EDO INNOVATE| NEWS",     
        return context

class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'news'
    template_name = 'pages/news-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = "EDO INNOVATE| NEWS",     
        return context