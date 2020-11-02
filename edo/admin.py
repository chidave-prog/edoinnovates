from django.contrib import admin
from .models import (Contact,
                    Programme,
                    Application,
                    Gallery,
                    Team,
                    Testimony,
                    Newsletter
                    )



admin.site.register(Programme)
admin.site.register(Application)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Testimony)
admin.site.register(Newsletter)
admin.site.register(Team)