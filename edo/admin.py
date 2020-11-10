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
                    Newsletter
                    )



admin.site.register(Programme)
admin.site.register(Application)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Testimony)
admin.site.register(Newsletter)
admin.site.register(Team)