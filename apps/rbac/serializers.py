# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 下午6:27
# @Author  : anonymous
# @File    : serializers.py
# @Software: PyCharm
# @Description:
from rest_framework import serializers
from .models import (User, Role, Menu)
from utils.base_model_serializer import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True, help_text='加入日期')

    class Meta:
        model = User
        exclude = ('is_deleted', 'first_name', 'last_name', 'email', 'is_staff')
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'last_login': {
                'read_only': True
            },
            'password': {
                'write_only': True
            },
            'is_superuser': {
                'read_only': True
            },
            'is_active': {
                'read_only': True
            },
            'avatar': {
                'read_only': True
            },
        }


class CurrentUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar', 'roles')
        extra_kwargs = {
            'username': {
                'read_only': True
            },
            'avatar': {
                'read_only': True
            },
            'roles': {
                'read_only': True
            },
        }
