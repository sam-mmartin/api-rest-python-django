from rest_framework import serializers
from site_api.models import Social

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

# class SocialByUserSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.name')
#     class Meta:
#         model = Social
#         fields = '__all__'