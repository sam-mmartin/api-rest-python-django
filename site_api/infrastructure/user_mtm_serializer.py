from rest_framework import serializers
from site_api.models import UserSocialMedia, UserLanguage

class UserSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSocialMedia
        fields = '__all__'

class UserLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLanguage
        fields = '__all__'