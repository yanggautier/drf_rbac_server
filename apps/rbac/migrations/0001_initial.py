# Generated by Django 3.1.7 on 2021-03-16 13:03

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import rbac.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='逻辑删除标记', verbose_name='逻辑删除标记')),
                ('menu_name', models.CharField(help_text='菜单名称', max_length=64, verbose_name='菜单名称')),
                ('menu_type', models.CharField(choices=[('1', '目录'), ('2', '菜单'), ('3', '按钮')], help_text='菜单类型', max_length=1, verbose_name='菜单类型')),
                ('is_outside_chain', models.BooleanField(default=False, help_text='是否外链', verbose_name='是否外链')),
                ('web_path', models.CharField(help_text='前端路由地址', max_length=256, verbose_name='前端路由地址')),
                ('parent_id', models.ForeignKey(blank=True, help_text='父菜单', null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.menu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '菜单管理',
                'verbose_name_plural': '菜单管理',
                'db_table': 'rbac_menu',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_deleted', models.BooleanField(default=False, help_text='逻辑删除标记', verbose_name='逻辑删除标记')),
                ('role_name', models.CharField(help_text='角色名称', max_length=64, verbose_name='角色名称')),
                ('status', models.BooleanField(default=True, help_text='角色状态', verbose_name='角色状态')),
                ('menus', models.ManyToManyField(help_text='权限列表', related_name='roles', to='rbac.Menu', verbose_name='权限列表')),
            ],
            options={
                'verbose_name': '角色管理',
                'verbose_name_plural': '角色管理',
                'db_table': 'rbac_role',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('department', models.CharField(blank=True, help_text='部门名称', max_length=64, verbose_name='部门名称')),
                ('position', models.CharField(blank=True, help_text='职位名称', max_length=64, verbose_name='职位名称')),
                ('phone', models.CharField(blank=True, help_text='手机号', max_length=11, verbose_name='手机号')),
                ('avatar', models.ImageField(blank=True, default='/images/default/default.jpeg', help_text='头像路径', upload_to=rbac.models.user_directory_path, verbose_name='头像路径')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roles', models.ManyToManyField(help_text='角色列表', related_name='users', to='rbac.Role', verbose_name='角色列表')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'rbac_user',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
