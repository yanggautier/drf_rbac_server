# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 下午6:20
# @Author  : anonymous
# @File    : urls.py
# @Software: PyCharm
# @Description:
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserModelViewSet, RoleModelViewSet, MenuModelViewSet, MyTokenObtainPairView

router = routers.DefaultRouter()
router.register(prefix=r'users', viewset=UserModelViewSet)
router.register(prefix=r'roles', viewset=RoleModelViewSet)
router.register(prefix=r'menus', viewset=MenuModelViewSet)
urlpatterns = [
    path('rbac/', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
