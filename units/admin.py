from django.contrib import admin

# Register your models here.
from .models import Area, City, Country, Furniture, Room, Unit ,Comments

class AreaAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'remarks']
    search_fields = ['title']

class CityAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'remarks']
    search_fields = ['title']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'remarks']
    search_fields = ['title']

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'remarks']
    search_fields = ['title']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'remarks']
    search_fields = ['title']

class UnitAdmin(admin.ModelAdmin):
    list_display  = ['id' , 'title' , 'country' , 'city' , 'area' , 'price' , 'active']
    list_filter   = ['active' , 'type']
    search_fields = ['title' , 'price']

admin.site.register(Area , AreaAdmin)
admin.site.register(City , CityAdmin)
admin.site.register(Country , CountryAdmin)
admin.site.register(Furniture , FurnitureAdmin)
admin.site.register(Room , RoomAdmin)
admin.site.register(Unit , UnitAdmin)
admin.site.register(Comments)