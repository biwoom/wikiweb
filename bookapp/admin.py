from django.contrib import admin
from django.conf import settings

# from .models import Book_BW
from .models import Publication_BW

# admin.site.register(Book_BW)

class Publication_BW_Admin(admin.ModelAdmin):
    list_display = ('id','main_title', 'volume', 'main_author', 'main_translator')


admin.site.register(Publication_BW, Publication_BW_Admin)