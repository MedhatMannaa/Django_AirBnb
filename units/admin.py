from django.contrib import admin

# Register your models here.
from .models import Area, City, Country, Furniture, Room, Unit

admin.site.register(Area)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Furniture)
admin.site.register(Room)
admin.site.register(Unit)