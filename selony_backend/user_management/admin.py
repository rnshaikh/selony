from django.contrib import admin

from django.contrib.auth.models import Permission

from user_management.models import User, Address


admin.site.register(User)
admin.site.register(Permission)
admin.site.register(Address)
