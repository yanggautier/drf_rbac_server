# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 下午9:45
# @Author  : anonymous
# @File    : custom_exception.py
# @Software: PyCharm
# @Description:
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError


def custom_exception_handler(exc, context):
    """
    自定义异常，需要在settings.py文件中进行全局配置
    1.在视图中的APIView中使用时,需要在验证数据的时候传入raise_exception=True说明需要使用自定义异常
    2.ModelViewSet中已经使用了raise_exception=True,所以无需配置
    """
    response = exception_handler(exc, context)
    # 对具体报错做兼容
    if isinstance(exc, ValidationError):
        response.data['code'] = response.status_code
        response.data['data'] = []
        if isinstance(response.data, dict):
            response.data['message'] = list(dict(response.data).values())[0][0]
            for key in dict(response.data).keys():
                if key not in ['code', 'data', 'message']:
                    response.data.pop(key)
        else:
            response.data['message'] = '输入有误'
        return response
    if response is not None:
        response.data.clear()
        response.data['code'] = response.status_code
        response.data['data'] = []
        if response.status_code == 404:
            try:
                response.data['message'] = response.data.pop('detail')
            except KeyError:
                response.data['message'] = '未找到'
        elif response.status_code == 400:
            response.data['message'] = '输入有误'
        elif response.status_code == 401:
            response.data['message'] = '未认证'
        elif response.status_code == 403:
            response.data['message'] = '没有权限'
        elif response.status_code == 405:
            response.data['message'] = '请求不允许'
        elif response.status_code == 500:
            response.data['message'] = '服务器错误'
        else:
            response.data['message'] = '未知错误'
    return response
