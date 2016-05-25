from django.contrib import admin
from .models import URLL,Author,Photo,Item

class AdminSetings(admin.ModelAdmin):
    list_display = ( 'url_adres', 'add_name')

class Photo_in_line(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [Photo_in_line]



admin.site.register(URLL,AdminSetings)
admin.site.register(Author)
admin.site.register(Item,ItemAdmin)
admin.site.register(Photo)
