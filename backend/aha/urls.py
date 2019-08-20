# -*- coding: utf-8 -*-
# author: itimor

from aha import settings
from aha.routerApi import router

from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_auth.views import PasswordChangeView
from django.views.generic.base import TemplateView
from rest_framework_jwt.views import obtain_jwt_token as jwt_token

urlpatterns = [
                  url(r'^api/', include(router.urls)),
                  # 用户认证
                  url(r'^api/changepasswd/', PasswordChangeView.as_view(), name='changepasswd'),
                  url(r'^api/api-token-auth/', jwt_token, name='rest_framework_token'),
                  url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  # url(r'', TemplateView.as_view(template_name="index.html")),
                  # django admin
                  url(r'^admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
