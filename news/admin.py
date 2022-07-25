from django.contrib import admin
from .models import Donation, News, Projects, MainCarousel, MainActivity


admin.site.register(News)
admin.site.register(Donation)
admin.site.register(Projects)
admin.site.register(MainCarousel)
admin.site.register(MainActivity)

