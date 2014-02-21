from django.contrib import admin
from .models import *


class AddressAdmin(admin.ModelAdmin):
    ''' Admin layout for Address'''
    pass

''' Register Admin layouts into django'''
admin.site.register(Address, AddressAdmin)
admin.site.register(Company)
admin.site.register(CompanyUser)
admin.site.register(SalesUser)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Chat)