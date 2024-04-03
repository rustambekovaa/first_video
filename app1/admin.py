from django.contrib import admin


from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    search_fielda = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')

admin.site.register(Women,WomenAdmin)


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fielda = ('name',)

admin.site.register(Category)

# Register your models here.
