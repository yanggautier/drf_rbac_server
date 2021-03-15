# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 下午6:20
# @Author  : anonymous
# @File    : urls.py
# @Software: PyCharm
# @Description:
from django.urls import path, include
from rest_framework import routers
from .views import UserModelViewSet

router = routers.DefaultRouter()
router.register(prefix=r'users', viewset=UserModelViewSet)
urlpatterns = [
    path('rbac/', include(router.urls))
]
