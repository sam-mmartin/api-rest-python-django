from django.contrib import admin
from site_api.models import User, Language, Social

class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'work')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class Languages(admin.ModelAdmin):
    list_display = ('id', 'name', 'startDateUse', 'level')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

class Socials(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'link')
    list_display_links = ('id', 'name', 'username')
    search_fields = ('name', 'username',)
    list_per_page = 10

admin.site.register(User, Users)
admin.site.register(Language, Languages)
admin.site.register(Social, Socials)