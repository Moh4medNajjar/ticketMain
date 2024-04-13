from rest_framework import serializers
from User.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'age',
            'field_of_interest',
            'phone',
            'email',
            'governorate',
            'is_verified',
            'is_admin',
            'cart',
            'tickets',
        ]
