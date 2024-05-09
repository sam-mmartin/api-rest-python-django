from rest_framework import viewsets, generics
from site_api.models import User, Language, Social
import site_api.infrastructure.users_serializer as user_serializer
import site_api.infrastructure.socials_serializer as socials_serializer
import site_api.infrastructure.languages_serializer as languages_serializer

""" Exibe todos os usuários """
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer.UserSerializer

""" Exibe todas as linguagens de programação """
class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = languages_serializer.LanguageSerializer

""" Exibe todas as redes sociais """
class SocialsViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = socials_serializer.SocialSerializer

""" Exibe todas as redes sociais de um usuário """
# class SocialsByUser(generics.ListAPIView):
#     def get_queryset(self):
#         queryset = Social.objects.filter(user=self.kwargs['pk'])
#         return queryset

#     serializer_class = socials_serializer.SocialByUserSerializer