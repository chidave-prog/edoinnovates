from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.contrib import messages
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

description=""
keywords=""

def Subscription(request):
    sub = request.POST.get("sub_email")
    exists = Newsletter.objects.filter(sub_email=sub).exists()
    print('\n',exists) 
    if sub and not exists:
        newsletter, created = Newsletter.objects.get_or_create(
            sub_email=sub,
            subscribe=True
        )
        newsletter.save()
        if request.is_ajax():          
            return JsonResponse({'form': "<i class='la la-thumbs-up'></i>  sucessfully subscribed!"})  
    else:
        if request.is_ajax(): 
            return JsonResponse({'form': "This Email is Already subscribed!"})       

   
    
def Search(request):
    context = {'title_tag': 'EDO INNOVATE: SEARCH PAGE'}
    opt = request.POST.get("opt")
    search = request.POST.get("search")
    if search and opt:
        if opt == 'programmes':
            search_result = Programme.objects.all().filter(
                Q(title__icontains=search)
                    | Q(description__icontains=search)
                    | Q(date_from__icontains=search)
                    | Q(date_to__icontains=search)
                    ,publish=True
            ).distinct()
            context.update({
                'search_result': search_result, 
                'keyword': search,               
            })           
            return render(request, 'pages/search.html', context)
        elif opt == 'news':
            search_result = Blog.objects.all().filter(
             Q(title__icontains=search)
            | Q(content__icontains=search)
            ,publish=True
            ).distinct()
            context.update({
                'search_result': search_result, 
                'keyword': search,              
            })           
            return render(request, 'pages/search.html', context)
    return render(request, 'pages/search.html', context)
        
def Contact(request):
    if request.POST.get("full_names") and request.POST.get("email") and request.POST.get("subject") and request.POST.get("message"):
        contact, created = Contact.objects.get_or_create(
            full_names=request.POST.get("full_names"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )
        contact.save()

        subject = str("Contact:  " + request.POST.get("subject") +
                        " from " + request.POST.get("full_names"))
        message = '%s' % (request.POST.get("message"))
        emailFrom = request.POST.get("email")
        emailTo = ['ohikhuemi@hotmail.com']
        send_mail(subject, message, emailFrom, emailTo,
                    fail_silently=True),
        messages.info(request,
                        "Thanks reaching-out to us. God Bless you.")
    if request.is_ajax():    
        return JsonResponse({'form': "Message Sent!"})



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