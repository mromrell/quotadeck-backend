from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')

    class Meta:
        model = User
        exclude = ('is_superuser', 'is_staff')

    def get_full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)



class AddressSerializer(serializers.ModelSerializer):
    """Serializes an Address object"""
    class Meta:
        model = Address

class ApplicationSerializer(serializers.ModelSerializer):
    """Serializes an Address object"""
    class Meta:
        model = Application

class CompanySerializer(serializers.ModelSerializer):
    """Serializes a Company object"""
    class Meta:
        model = Company

class CompanyUserSerializer(serializers.ModelSerializer):
    """Serializes a CompanyUser object"""
    class Meta:
        model = CompanyUser

class SalesUserSerializer(serializers.ModelSerializer):
    """Serializes a SalesUser object"""
    class Meta:
        model = SalesUser


class JobSerializer(serializers.ModelSerializer):
    """Serializes a Job object"""
    class Meta:
        model = Job
        model

class ApplicationSerializer(serializers.ModelSerializer):
    """Serializes a Application object"""
    class Meta:
        model = Application

class ChatSerializer(serializers.ModelSerializer):
    """Serializes a Chat object"""
    class Meta:
        model = Chat