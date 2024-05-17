from rest_framework import serializers
from site_api.models import User, Social, Language, UserSocialMedia, UserLanguage
from .socials_serializer import SocialSerializer
from .languages_serializer import LanguageSerializer
from .function import attemp_json_deserialize

class UserSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)
    socials_medias = SocialSerializer(many=True)

    class Meta:
        model = User
        fields = ['id',
                  'name',
                  'username',
                  'email',
                  'work',
                  'languages',
                  'socials_medias'
                  ]

    def create(self, validated_data):
        languages_data = validated_data.pop('languages')
        socials_data = validated_data.pop('socials_medias')

        languages_data = attemp_json_deserialize(languages_data,
                                                 expect_type=list)
        socials_data = attemp_json_deserialize(socials_data,
                                               expect_type=list)

        user = User.objects.create(**validated_data)

        for language in languages_data:
            new_language = Language.objects.create(**language)
            UserLanguage.objects.create(user = user, language=new_language)

        for social in socials_data:
            new_social = Social.objects.create(**social)
            UserSocialMedia.objects.create(user=user, social=new_social)

        return user

    def update(self, instance: User, validated_data):
        socials_data = validated_data.pop('socials_medias')
        socials_data = attemp_json_deserialize(socials_data, expect_type=list)

        for social in socials_data:
            try:
                obj = UserSocialMedia.objects.filter(
                    social__name=social['name']).filter(
                        social__username=social['username'])

                if obj.count() == 0:
                    social_objs = Social.objects.filter(
                        name=social['name']).filter(
                            username=social['username'])

                    if social_objs.count() == 0:
                        new_social = Social.objects.create(**social)
                        UserSocialMedia.objects.create(user=instance, social=new_social)
            except:
                pass

        instance.save()

        return instance