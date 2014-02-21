from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializes a User object"""
    class Meta:
        model = User
        fields = ('id', 'username')


class AddressSerializer(serializers.ModelSerializer):
    """Serializes an Address object"""
    class Meta:
        model = Address

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

class ApplicationSerializer(serializers.ModelSerializer):
    """Serializes a Application object"""
    class Meta:
        model = Application

class ChatSerializer(serializers.ModelSerializer):
    """Serializes a Chat object"""
    class Meta:
        model = Chat