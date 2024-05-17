from rest_framework import serializers
from site_api.models import UserSocialMedia, UserLanguage
from .users_serializer import UserSerializer
from .socials_serializer import SocialSerializer
from .languages_serializer import LanguageSerializer

class UserSocialMediaSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    social = SocialSerializer()

    class Meta:
        model = UserSocialMedia
        fields = '__all__'

class UserLanguageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    language = LanguageSerializer()

    class Meta:
        model = UserLanguage
        fields = '__all__'