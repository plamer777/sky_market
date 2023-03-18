"""This unit contains serializers to implement CRUD operations with User
model"""
from djoser.serializers import UserCreateSerializer as \
    BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
# --------------------------------------------------------------------------

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """UserRegistrationSerializer serves to add new user in the database"""
    password = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = User
        exclude = ('last_login', 'role', 'is_active', 'id')


class UserSerializer(BaseUserRegistrationSerializer):
    """The UserSerializer serves to implement all operations except
    registration"""
    class Meta:
        model = User
        exclude = ('last_login', 'role', 'is_active')

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password'))
        instance.save()
        return super().update(instance, validated_data)


class CurrentUserSerializer(serializers.ModelSerializer):
    """This serializer serves to work with current user and to implement
     CRUD operations with current user"""
    class Meta:
        model = User
        exclude = ('last_login', 'role', 'is_active')

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password'))
        instance.save()
        return super().update(instance, validated_data)

