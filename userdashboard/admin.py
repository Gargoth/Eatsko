from django.contrib import admin
from .models import FoodGenre, Profile, Eatery, Menu
# Register your models here.

admin.site.register(FoodGenre)
admin.site.register(Profile)
admin.site.register(Eatery)
admin.site.register(Menu)
