from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.base_model import BaseModel


def user_directory_path(instance, filename):
    """
    自定义用户头像保存路径为：static/media/images/user_<id>/<filename>
    """
    return f'{instance.user.id}/{filename}'


# Create your models here.
class User(AbstractUser):
    """
    用户表rbac_user模型
    blank=True在字符串类型的字段上表现为空字符串，不是null
    """
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')
    department = models.CharField(max_length=64, blank=True, verbose_name='部门名称', help_text='部门名称')
    position = models.CharField(max_length=64, blank=True, verbose_name='职位名称', help_text='职位名称')
    phone = models.CharField(max_length=11, blank=True, verbose_name='手机号', help_text='手机号')
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, default='/images/default/default.jpeg',
                               verbose_name='头像路径', help_text='头像路径')
    roles = models.ManyToManyField(to='Role', related_name='users', verbose_name='角色列表', help_text='角色列表')

    class Meta:
        db_table = 'rbac_user'
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'
        ordering = ['id']

    def __str__(self):
        return self.username


class Role(BaseModel):
    role_name = models.CharField(max_length=64, verbose_name='角色名称', help_text='角色名称')
    status = models.BooleanField(default=True, verbose_name='角色状态', help_text='角色状态')
    menus = models.ManyToManyField(to='Menu', related_name='roles', verbose_name='权限列表', help_text='权限列表')

    class Meta:
        db_table = 'rbac_role'
        verbose_name = '角色管理'
        verbose_name_plural = '角色管理'
        ordering = ['id']

    def __str__(self):
        return self.role_name


class Menu(BaseModel):
    MENU_TYPE_CHOICES = (
        ("1", "目录"),
        ("2", "菜单"),
        ("3", "按钮"),
    )
    parent_id = models.ForeignKey(to='self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='父菜单',
                                  help_text='父菜单')
    menu_name = models.CharField(max_length=64, verbose_name='菜单名称', help_text='菜单名称')
    menu_type = models.CharField(max_length=1, choices=MENU_TYPE_CHOICES, verbose_name='菜单类型', help_text='菜单类型')
    is_outside_chain = models.BooleanField(default=False, verbose_name="是否外链", help_text='是否外链')
    web_path = models.CharField(max_length=256, verbose_name="前端路由地址", help_text='前端路由地址')

    class Meta:
        db_table = 'rbac_menu'
        verbose_name = '菜单管理'
        verbose_name_plural = '菜单管理'
        ordering = ['id']

    def __str__(self):
        return self.menu_name
