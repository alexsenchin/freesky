from django.contrib import admin
from .models import Donation, News, Projects, MainCarousel, MainActivity, PaymentDetails, Contacts


admin.site.register(News)
admin.site.register(Donation)
admin.site.register(Projects)
admin.site.register(MainCarousel)
admin.site.register(MainActivity)
admin.site.register(PaymentDetails)
admin.site.register(Contacts)

