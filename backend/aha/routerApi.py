# -*- coding: utf-8 -*-
# author: timor

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from users.views import UserViewSet, RoleViewSet

router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

from tools.views import UploadViewSet, FileUploadViewSet

router.register(r'uploads', UploadViewSet)
router.register(r'fileuploads', FileUploadViewSet)
