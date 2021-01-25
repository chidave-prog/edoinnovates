from django.contrib import admin
from .models import (
    Contact,
    Programme,
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


# admin.site.register(Programme)
admin.site.register(Application)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Gallery)
# admin.site.register(Contact)
admin.site.register(Testimony)
admin.site.register(Newsletter)
admin.site.register(Team)


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('full_names', 'email', 'subject', 'created_at',)

@admin.register(Programme)
class Programme(admin.ModelAdmin):
    list_display = ('title', 'publish', 'created_at',)

@admin.register(StartupsdAndHubs)
class StartupsdAndHubs(admin.ModelAdmin):
    list_display = ('category', 'name', 'publish', 'created_at',)

@admin.register(Hall)
class Hall(admin.ModelAdmin):
    list_display = ('name', 'publish', 'slug', 'created_at',)