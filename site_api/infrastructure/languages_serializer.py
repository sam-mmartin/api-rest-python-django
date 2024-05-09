from rest_framework import serializers
from site_api.models import Language

class LanguageSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()

    class Meta:
        model = Language
        fields = '__all__'

    def get_level(self, obj):
        return obj.get_level_display()