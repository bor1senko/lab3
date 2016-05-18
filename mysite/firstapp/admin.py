from django.contrib import admin
from .models import URLL,Author

class AdminSetings(admin.ModelAdmin):
    list_display = ( 'url_adres', 'add_name')

admin.site.register(URLL,AdminSetings)
admin.site.register(Author)
