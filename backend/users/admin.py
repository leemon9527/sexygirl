# -*- coding: utf-8 -*-
# author: itimor

from django.contrib import admin
from users.models import User, Role


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'avator', 'create_date', 'is_active', 'is_admin')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)
