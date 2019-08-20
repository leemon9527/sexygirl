# -*- coding: utf-8 -*-
# author: timor

from rest_framework import viewsets
from users.serializers import UserSerializer, RoleSerializer
from users.models import User, Role
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'email']
    filter_fields = ['username']


class RoleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_fields = ['name']
