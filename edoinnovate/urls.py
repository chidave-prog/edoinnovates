from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

urlpatterns = [
    path('mrasemota/', admin.site.urls),
    path('', include('edo.urls')),
    path('webdesignbootcamp/', include('web_bootcamp.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
admin.site.site_header = "EDO INNOVATE"
admin.site.site_title = "EDO INNOVATE"
admin.site.index_title = "EDO INNOVATE (Staff-Only)"
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
