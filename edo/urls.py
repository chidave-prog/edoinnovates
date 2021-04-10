from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic import RedirectView


from .views import (Home, Subscription, Search, ContactPage, AwsRestartBenin, GalleryDetailView, BlogListView,
                    BlogDetailView, Halls, IndexView, ProgrammeDetailView, MSPowerApps,
                    StartupsdAndHubsDetailView, About,
                    HallsDetailView)


urlpatterns = [
    # path('index/', Home, name='home'),
    path('', IndexView.as_view(), name='index'),
    path('programme/<slug>/', ProgrammeDetailView.as_view(), name='programme'),
    path('smes/<slug>/', StartupsdAndHubsDetailView.as_view(),
         name='startupsdsndhub'),
    path('hall/<slug>/', HallsDetailView.as_view(), name='hall'),
    path('newsletter/', Subscription, name='newsletter'),
    path('about/', About, name='about'),
    path('search/', Search, name='search'),
    path('contact/', ContactPage, name='contact'),
    path('aws-restart-edo/', AwsRestartBenin, name='aws-restart-edo'),
    path('ms-power-apps/', MSPowerApps, name='mspower-apps'),
    path('gallery/<slug>/', GalleryDetailView.as_view(), name='gallery-detail'),
    path('halls/', Halls, name='halls'),
    path('news/', BlogListView.as_view(), name='news'),
    path('news/<slug>/', BlogDetailView.as_view(), name='blog-detail'),
]
