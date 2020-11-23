from django.urls import path, include, re_path
from django.conf.urls import url
from .views import (Home,Subscription, Search, ContactPage, AwsRestartBenin,GalleryDetailView, BlogListView, 
BlogDetailView)


urlpatterns = [
    path('', Home, name='home'), 
    path('newsletter/', Subscription, name='newsletter'), 
    path('search/', Search, name='search'),
     path('contact/', ContactPage, name='contact'), 
    path('aws-restart-edo/', AwsRestartBenin, name='aws-restart-edo'),  
    path('gallery/<slug>/', GalleryDetailView.as_view(),name='gallery-detail'),
    path('news/', BlogListView.as_view(),name='news'),
    path('news/<slug>/', BlogDetailView.as_view(),name='blog-detail'),
]

