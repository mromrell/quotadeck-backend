from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django.core.context_processors import csrf
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.models import User
from .models import *
from .serializers import *


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class UserList(generics.ListCreateAPIView):
    """List all users or create a new User"""
    permission_classes = (permissions.IsAuthenticated,)
    # TODO: Figure out this permission class
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a User instance."""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer

class JobDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a User instance."""
    model = Job
    serializer_class = JobSerializer

class CompanyUserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a CompanyUser instance."""
    permission_classes = (permissions.IsAuthenticated,)
    model = CompanyUser
    serializer_class = CompanyUserSerializer

class CompanyDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a CompanyUser instance."""
    # permission_classes = (permissions.IsAuthenticated,)
    model = Company
    serializer_class = CompanySerializer

class SalesUserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a SalesUser instance."""
    # permission_classes = (permissions.IsAuthenticated,)
    model = SalesUser
    serializer_class = SalesUserSerializer

class ApplicationList(generics.RetrieveAPIView):
    """Retrieve, update or delete a SalesUser instance."""
    model = Application
    serializer_class = ApplicationSerializer


class AddressList(generics.ListCreateAPIView):
    """List all addresses or create a new Address"""
    permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an Address."""
    # permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer

class CompanyList(generics.ListCreateAPIView):
    """List all Companies or create a new company"""
    #permission_classes = (permissions.IsAuthenticated,)
    model = Company
    serializer_class = CompanySerializer

class ChatList(generics.ListCreateAPIView):
    """List all Chat or create a new Chat"""
    #permission_classes = (permissions.IsAuthenticated,)
    model = Chat
    serializer_class = ChatSerializer

class JobList(generics.ListCreateAPIView):
    """List all Jobs or create a new Job"""
    #permission_classes = (permissions.IsAuthenticated,)
    model = Job
    serializer_class = JobSerializer

@api_view(('POST',))
def authenticate(request):
    c = {}
    c.update(csrf(request))

    username = request.POST.get('username', request.DATA['username'])  # emtpy string if no username exists
    password = request.POST.get('password', request.DATA['password'])  # empty string if no password exists

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    else:
        c['message'] = 'Login failed!'
        return render_to_response('partials/login.tpl.html', c)


def logout(request):
    auth.logout(request)
    return JSONResponse([{'success': 'Logged out!'}])