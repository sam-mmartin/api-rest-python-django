from django.contrib import admin
from django.urls import path

from site_api.views import users

urlpatterns = [
    path('users/', users),
    path('admin/', admin.site.urls),
]
