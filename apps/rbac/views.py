from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.custom_model_view_set import CustomModelViewSet
from .serializers import UserSerializer, CurrentUserInfoSerializer, RoleSerializer, MenuSerializer, \
    MyTokenObtainPairSerializer
from .models import User, Role, Menu
from utils.custom_json_response import JsonResponse


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    ordering_fields = ('id',)

    @action(detail=False)
    def info(self, request):
        """
        获取某个用户的简略信息,包含id、用户名、头像路径、角色列表
        """
        data = User.objects.filter(id=request.user.id)
        serializer = self.get_serializer(data, many=True)
        return JsonResponse(data=serializer.data, code=200, msg='success', status=status.HTTP_200_OK)

    def get_serializer_class(self):
        """
        不同的action使用不同的序列化器
        """
        return CurrentUserInfoSerializer if self.action == 'info' else self.serializer_class


class RoleModelViewSet(CustomModelViewSet):
    queryset = Role.objects.filter(is_deleted=False)
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAdminUser,)
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
