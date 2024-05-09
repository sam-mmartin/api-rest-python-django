from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from site_api.views import UsersViewSet, SocialsViewSet, LanguagesViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='Usuários')
router.register('languages', LanguagesViewSet, basename='Linguagens')
router.register('socials', SocialsViewSet, basename='Redes Sociais')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

#path('users/<int:pk>/socials/', SocialsByUser.as_view())