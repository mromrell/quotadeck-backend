"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = patterns(
    'apps.public.views',
    url(r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^api/users$', 'authenticate'),
    url(r'^api/user$', 'logout'),

    url(r'^addresses$', AddressList.as_view(), name='address-list'),
    url(r'^addresses/(?P<pk>[0-9]+)$', AddressDetail.as_view(), name='address-detail'),
    url(r'^users$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),

    url(r'^companies$', CompanyList.as_view(), name='company-list'),
    # url(r'^company$', CompanyDetail.as_view(), name='company-detail'),
    url(r'^company/(?P<pk>[0-9]+)$', CompanyDetail.as_view(), name='company-list'),
    url(r'^company-user/(?P<pk>[0-9]+)$', CompanyUserDetail.as_view(), name='company-user-detail'),

    url(r'^applications/(?P<pk>[0-9]+)$', ApplicationList.as_view(), name='application-list'),
    url(r'^chat/(?P<pk>[0-9]+)$', ChatList.as_view(), name='chat-list'),
    url(r'^sales-user/(?P<pk>[0-9]+)$', SalesUserDetail.as_view(), name='Sales-user-detail'),


    url(r'^job$', JobList.as_view(), name='job-list'),
    url(r'^job-details/(?P<pk>[0-9]+)$', JobDetail.as_view(), name='job-detail'),
)

urlpatterns += patterns('', url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'))

urlpatterns = format_suffix_patterns(urlpatterns)