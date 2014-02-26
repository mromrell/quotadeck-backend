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
from rest_framework.authtoken.views import ObtainAuthToken

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

class ApplicationDetail(generics.ListCreateAPIView):
    """List all Application or create a new Address"""
    model = Application
    serializer_class = ApplicationSerializer


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


@api_view(('GET', ))
def getJobs(request):
    jobs_list = JobList.object.all()
    company_list = []
    new_list = {}

    for job in jobs_list:
        company_list.append(Company.object.one(job.company))


class NewAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])
            data = {
                'user': UserSerializer(User.objects.filter(auth_token=token)).data,
                'token': token.key,
                }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('POST',))
# @permission_classes((IsAdmin,))
def custom_new_user(request):
    request.DATA['username'] = request.DATA['email']
    user = UserSerializer(data=request.DATA)

    if user.is_valid():
        user.save()
    else:
        if 'username' in user.errors and user.errors['username'] == ['User with this Username already exists.']:
            return Response({'errors': { 'email': ['User with this e-mail already exists.']}}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'errors': user.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(user.data)



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

@api_view(('GET',))
def uploadedimages(request, location_id):
    location = Location.objects.get(id=location_id)
    photo_name = location.photos.name.split("/")[-1]
    # if request.method == 'GET':
    #     logo = Logo.objects.get(consultant_id=company.consultant_id)
    if request.is_secure():
        photo_url = ''.join(['https://', request.META['HTTP_HOST'], '/static/', photo_name])
    else:
        photo_url = ''.join(['http://', request.META['HTTP_HOST'], '/static/', photo_name])

    response = [photo_url, location_id]
    return Response(response)

def logout(request):
    auth.logout(request)
    return JSONResponse([{'success': 'Logged out!'}])

# @api_view(('GET',))
# def user_leadsources(request, pk):
#     lead_source_list = LeadSource.objects.filter(created_by=pk)
#     serialize = LeadSourceSerializer(lead_source_list)
#     return Response(serialize.data)

@api_view(('GET',))
def jobs_list(request, pk):
    lead_source_list = LeadSource.objects.filter(created_by=pk)
    serialize = LeadSourceSerializer(lead_source_list)
    return Response(serialize.data)
