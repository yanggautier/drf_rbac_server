from rest_framework import permissions, status
from rest_framework.decorators import action
from utils.custom_model_view_set import CustomModelViewSet
from .serializers import UserSerializer, CurrentUserInfoSerializer, RoleSerializer, MenuSerializer
from .models import User, Role, Menu
from utils.custom_json_response import JsonResponse


# Create your views here.
class UserModelViewSet(CustomModelViewSet):
    """
    list:
    返回用户(多个)列表数据

    create:
    创建用户

    retrieve:
    返回用户(单个)详情数据

    update:
    更新(全部信息)用户

    partial_update:
    更新(部分信息)用户

    destroy:
    删除单个用户

    info:
    返回某个用户的简略信息
    """
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    ordering_fields = ('id',)

    def perform_destroy(self, instance):
        """
        逻辑删除
        """
        instance.is_deleted = True
        instance.save()

    @action(detail=True, methods=['get'])
    def info(self, request, pk=None):
        """
        获取某个用户的简略信息,包含id、用户名、头像路径、角色列表
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(data=serializer.data, code=1/0, msg='success', status=status.HTTP_200_OK)

    def get_serializer_class(self):
        """
        不同的action使用不同的序列化器
        """
        return CurrentUserInfoSerializer if self.action == 'info' else self.serializer_class


class RoleModelViewSet(CustomModelViewSet):
    queryset = Role.objects.filter(is_deleted=False)
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated,)
    ordering_fields = ('id',)

    def perform_destroy(self, instance):
        """
        逻辑删除
        """
        instance.is_deleted = True
        instance.save()


class MenuModelViewSet(CustomModelViewSet):
    queryset = Menu.objects.filter(is_deleted=False)
    serializer_class = MenuSerializer
    permission_classes = (permissions.IsAdminUser,)
    ordering_fields = ('id',)

    def perform_destroy(self, instance):
        """
        逻辑删除
        """
        instance.is_deleted = True
        instance.save()
