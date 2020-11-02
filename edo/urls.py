from django.urls import path, include, re_path
from django.conf.urls import url
from .views import (Home, AwsRestartBenin     )


urlpatterns = [
    path('', Home, name='home'), 
    path('aws-restart-Benin/', AwsRestartBenin, name='aws-restart-Benin'),  
]

