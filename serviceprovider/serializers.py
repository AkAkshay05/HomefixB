# from rest_framework import serializers
# from .models import ServiceProvider
#
# class ServiceProviderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceProvider
#         fields = '__all__'
from rest_framework import serializers
from .models import ServiceProvider
from django.contrib.auth.hashers import make_password

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
