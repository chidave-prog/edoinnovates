from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic
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
    Newsletter,
    StartupsdAndHubs,
    Hall
)
from decor.models import Pageslider
from .forms import (CommentForm, CommentReplyForm)

description = ""
keywords = ""


class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        context = {
        'title_tag': "EDO INNOVATE| Touching Lives",  
        "programmes": Programme.objects.filter(publish=True).order_by('-created_at'),
        "startup": StartupsdAndHubs.objects.filter(publish=True, category="start_up").order_by('-created_at'),
        "hubs": StartupsdAndHubs.objects.filter(publish=True, category="hub").order_by('-created_at'),
        "halls": Hall.objects.filter(publish=True).order_by('-created_at'),
        }

        return render(request, "contents/home.html", context)



class ProgrammeDetailView(generic.DetailView):
    model = Programme
    context_object_name = 'programme'
    template_name = 'contents/programmes.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = str(self.object.title)               
        return context

class StartupsdAndHubsDetailView(generic.DetailView):
    model = StartupsdAndHubs
    context_object_name = 'startupsdsndhub'
    template_name = 'contents/startupsdsndhubs.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = str(self.object.name)               
        return context
    
class HallsDetailView(generic.DetailView):
    model = Hall
    context_object_name = 'hall'
    template_name = 'contents/hall.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_tag'] = str(self.object.name)               
        return context

   
def Subscription(request):
    sub = request.POST.get("sub_email")
    exists = Newsletter.objects.filter(sub_email=sub).exists()    
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
                | Q(description__icontains=search), publish=True
            ).distinct()
            context.update({
                'search_result': search_result,
                'keyword': search,
            })
            return render(request, 'pages/search.html', context)
        elif opt == 'news':
            search_result = Blog.objects.all().filter(
                Q(title__icontains=search)
                | Q(content__icontains=search), publish=True
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
        message = '%s %s %s %s' % (request.POST.get(
            "message"), "\n from: \n", request.POST.get('full_names'), "\n email: " + str(request.POST.get("email")))
        emailFrom = request.POST.get("email")
        emailTo = ['asemotaizoduwa@edojobs.org',
                   'believe.ohiozua@gmail.com', 'awsrestartedo@gmail.com']
        send_mail(subject, message, emailFrom, emailTo,
                  fail_silently=True),
        if request.is_ajax():
            return JsonResponse({'form': "Message Sent!"})
    return render(request, 'pages/contactpage.html', {})


def Home(request):
    context = {
        'title_tag': "EDO INNOVATE| Touching Lives",
        'training': Programme.objects.filter(publish=True, programme_type="TRAINING").order_by('-created_at'),
        'competition': Programme.objects.filter(publish=True, programme_type="COMPETITION").order_by('-created_at'),
        'scholarship': Programme.objects.filter(publish=True, programme_type="SCHOLARSHIP").order_by('-created_at'),
        'opportunity': Programme.objects.filter(publish=True, programme_type="OPPORTUNITY").order_by('-created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'gallery': Gallery.objects.filter(publish=True).order_by('-created_at'),
        'blog': Blog.objects.filter(publish=True).order_by('-created_at')[:4],
        'team': Team.objects.filter(publish=True, office='Borad_members').order_by('-created_at'),
        'pageslider': Pageslider.objects.filter(publish=True),
    }
    return render(request, 'pages/index.html', context)


def Halls(request):
    context = {
        'title_tag': "EDO INNOVATE| Halls",
        'training': Programme.objects.filter(publish=True, programme_type="TRAINING").order_by('-created_at'),
        'competition': Programme.objects.filter(publish=True, programme_type="COMPETITION").order_by('-created_at'),
        'scholarship': Programme.objects.filter(publish=True, programme_type="SCHOLARSHIP").order_by('-created_at'),
        'opportunity': Programme.objects.filter(publish=True, programme_type="OPPORTUNITY").order_by('-created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'gallery': Gallery.objects.filter(publish=True, photo_type='halls').order_by('-created_at'),
        'blog': Blog.objects.filter(publish=True).order_by('-created_at')[:4],
        'team': Team.objects.filter(publish=True, office='Borad_members').order_by('-created_at'),
        'pageslider': Pageslider.objects.filter(publish=True),
    }
    return render(request, 'pages/halls.html', context)


def AwsRestartBenin(request):
    return render(request, 'contents/aws-restart-edo.html', {})
    # return redirect('/programme/aws-restart-edo/')

def About(request):
    # return render(request, 'pages/about.html', {})
    context = {
        'title_tag': "EDO INNOVATE| AWS Re/Start Benin",
        'programme': Programme.objects.all().order_by('created_at'),
        'gallery': Gallery.objects.all().order_by('created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'blog': Blog.objects.filter(publish=True).order_by('-created_at')[:4],
        'team': Team.objects.filter(publish=True, office='aws_instructors').order_by('-created_at'),
    }
    return render(request, 'pages/about.html', context)


def ComputerAppreciation(request):
    context = {
        'title_tag': "EDO INNOVATE| Computer Appreciation",
        'programme': Programme.objects.all().order_by('created_at'),
        'gallery': Gallery.objects.all().order_by('created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'blog': Blog.objects.filter(publish=True).order_by('-created_at')[:4],       
    }
    return render(request, 'pages/computerappreciation.html', context)


def PluralSite(request):
    context = {
        'title_tag': "EDO INNOVATE| Plural Site",
        'programme': Programme.objects.all().order_by('created_at'),
        'gallery': Gallery.objects.all().order_by('created_at'),
        'testimonies': Testimony.objects.filter(publish=True).order_by('-created_at'),
        'blog': Blog.objects.filter(publish=True).order_by('-created_at')[:4],       
    }
    return render(request, 'pages/pluralsite.html', context)

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
        view = Blog.objects.get(pk=self.get_object().pk)
        if view:
            view.views = int(view.views) + 1
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
