# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 下午6:27
# @Author  : anonymous
# @File    : serializers.py
# @Software: PyCharm
# @Description:
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import (User, Role, Menu)
from utils.base_model_serializer import BaseModelSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        """
        重写validate方法，返回自己手动生成的token
        :param attrs:
        :return:
        """
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['code'] = 200
        return data


class UserSerializer(BaseModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True, help_text='加入日期')

    class Meta:
        model = User
        exclude = ('first_name', 'last_name', 'is_staff')
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

    def to_representation(self, instance):
        """
        自定义多对多字段列表的返回数据格式
        """
        representation = super().to_representation(instance)
        representation['roles'] = RoleSerializer(instance.roles, many=True).data
        return representation

    def create(self, validated_data):
        """
        创建用户时设置密码为密文
        """
        instance = super().create(validated_data)
        instance.set_password(self.validated_data['password'])
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        修改用户时设置密码为密文
        """
        instance = super().update(instance, validated_data)
        instance.set_password(self.validated_data['password'])
        instance.save()
        return instance


class CurrentUserInfoSerializer(serializers.ModelSerializer):
    """
    获取当前登录用户信息序列化器
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'avatar', 'roles')
        extra_kwargs = {
            'id': {
                'read_only': True
            },
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

    def to_representation(self, instance):
        """
        自定义多对多字段列表的返回数据格式
        """
        representation = super().to_representation(instance)
        representation['roles'] = [item.get('role_name') for item in RoleSerializer(instance.roles, many=True).data]
        return representation


class RoleSerializer(BaseModelSerializer):
    class Meta:
        model = Role
        exclude = ('is_deleted',)
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def to_representation(self, instance):
        """
        自定义多对多字段列表的返回数据格式
        """
        representation = super().to_representation(instance)
        representation['menus'] = MenuSerializer(instance.menus, many=True).data
        return representation


class MyCharField(serializers.CharField):
    """
    自定义字段：在`一对多关系`中, 用于在`一的一方`反查`多的一方`的数据, 数据可自定制
    注意：在序列化器类中使用该字段时, 不能在extra_kwargs中定义该字段的属性值, 即使定义了也不会生效
    """

    def to_representation(self, value):
        data_list = []
        for row in value:
            data_list.append({'id': row.id, 'menu_name': row.menu_name})
        return data_list


class MenuSerializer(BaseModelSerializer):
    child_menus = MyCharField(source='menu_set.all', help_text='父级菜单', label='父级菜单', read_only=True)

    class Meta:
        model = Menu
        exclude = ('is_deleted',)
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    def to_representation(self, instance):
        """
        自定义多对多字段列表的返回数据格式
        """
        representation = super().to_representation(instance)
        representation['parent_menu_name'] = MenuSerializer(instance.parent_id).data.get('menu_name')
        return representation
