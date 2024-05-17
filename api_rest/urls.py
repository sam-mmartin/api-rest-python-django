from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from site_api.views import UsersViewSet, SocialsViewSet, LanguagesViewSet
from site_api.orm_views.socials_with_users_view import SocialsWithUsersView

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('languages', LanguagesViewSet, basename='Linguagens')
router.register('socials', SocialsViewSet, basename='Redes Sociais')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('socials/users/',
         SocialsWithUsersView.as_view({'get': 'get'}),
         name='Usuários e Redes Sociais'),
    path('socials/users/<str:username>/',
         SocialsWithUsersView.as_view({'get': 'get_by_username'}),
         name='get_by_username'),
    path('', include(router.urls)),
]