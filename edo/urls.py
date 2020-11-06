from django.urls import path, include, re_path
from django.conf.urls import url
from .views import (Home,Newsletter, Search, Contact, AwsRestartBenin,GalleryDetailView, BlogListView, 
BlogDetailView)


urlpatterns = [
    path('', Home, name='home'), 
    path('newsletter/', Newsletter, name='newsletter'), 
    path('search/', Search, name='search'),
     path('contact/', Contact, name='contact'), 
    path('aws-restart-Benin/', AwsRestartBenin, name='aws-restart-Benin'),  
    path('gallery/<slug>/', GalleryDetailView.as_view(),name='gallery-detail'),
    path('news/', BlogListView.as_view(),name='news'),
    path('news/<slug>/', BlogDetailView.as_view(),name='blog-detail'),
]

