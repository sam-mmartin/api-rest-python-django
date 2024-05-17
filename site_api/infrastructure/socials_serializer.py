from rest_framework import serializers
from site_api.models import Social

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'