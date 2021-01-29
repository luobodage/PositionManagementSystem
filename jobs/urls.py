# -*- coding: UTF-8 -*-
from django.conf.urls import url
from jobs import views

# 注册到url路径里
urlpatterns = [
    # 职位列表
    url(r"^joblist/", views.joblist, name='joblist') # 使用正则来匹配url路径 以joblist开头的 就跳转
]

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/1/28 18:37
# software: PyCharm
#         =    =     =
#          =   =   =
#           =  =  =
#         ===========
#         =   萝    =
#         =   卜    =
#         =   神    =
#         =   保    =
#         =   佑    =
#         =   永    =
#         =   无    =
#         =   bug  =
#          =      =
#           =    =
#              =
