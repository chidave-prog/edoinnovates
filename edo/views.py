from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
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
from decor.models import Pageslider

from .forms import (CommentForm, CommentReplyForm)
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
        
def ContactPage(request):
    if request.POST.get("full_names") and request.POST.get("email") and request.POST.get("subject") and request.POST.get("message"):
        contact, created = Contact.objects.get_or_create(
            full_names=request.POST.get("full_names"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )
        contact.save()

        subject = f"Contact Message From Edo Innovate Site:  {request.POST.get('subject')}" 
        message = '%s %s %s' % (request.POST.get("message"), "\n from: \n", request.POST.get('full_names'))
        emailFrom = request.POST.get("email")
        emailTo = ['asemotaizoduwa@edojobs.org', 'believe.ohiozua@gmail.com']
        send_mail(subject, message, emailFrom, emailTo,
                    fail_silently=True),      
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
        'pageslider': Pageslider.objects.filter(publish=True),
    }
    return render(request, 'pages/index.html', context)



def AwsRestartBenin(request):     
    context={
        'title_tag'  : "EDO INNOVATE| AWS Re/Start Benin",
        'programme': Programme.objects.all().order_by('created_at'),
        'gallery': Gallery.objects.all().order_by('created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'blog': Blog.objects.filter(publish=True).order_by('-created_at')[:4],
        'team': Team.objects.filter(publish=True, office='aws_instructors').order_by('-created_at'),
    }
    return render(request, 'pages/aws.html', context)


class GalleryDetailView(generic.DetailView):
    model = Gallery
    context_object_name = 'gallery'
    template_name = 'pages/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = "EDO INNOVATE| Gallery"     
        return context

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 8
    context_object_name = 'news'
    template_name = 'pages/news_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = "EDO INNOVATE| NEWS"    
        return context
    

class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'news'
    template_name = 'pages/news-details.html'
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        view=Blog.objects.get(pk=self.get_object().pk)
        if view:
            view.views= int(view.views) + 1
            view.save() 
        context['title_tag'] = "EDO INNOVATE| NEWS" 
        context['form'] = CommentForm
        context['replyForm'] = CommentReplyForm    
        return context
    
    def post(self, request, *args, **kwargs):
        blog_id = self.get_object()
        form = CommentForm(request.POST)
        reply = CommentReplyForm(request.POST)
        if form.is_valid():
            form.instance.blog = blog_id
            form.save()
            messages.info(request,
                          "Thanks For Your Comment.")            
            return redirect(reverse("blog-detail", kwargs={'slug': blog_id.slug}))

        if reply.is_valid():
            target_comment = request.POST.get('target_comment')
            add_reply = Comment.objects.get(pk=target_comment)
            add_reply.user = request.user
            add_reply.reply = request.POST.get('reply')
            add_reply.replyed = True
            add_reply.save()
            messages.info(request,
                          "You Have Replied")           
            return redirect(reverse("blog-detail", kwargs={'slug': blog_id.slug}))
