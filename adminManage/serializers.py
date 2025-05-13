from rest_framework import serializers
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        admin = Admin.objects.create_admin(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return admin
