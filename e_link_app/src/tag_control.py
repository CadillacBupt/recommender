# -*- coding:utf-8 -*-

#模型导入
from e_link_app.models import *
#异常导入
from django.core.exceptions import ObjectDoesNotExist
#日志导入
import logging
#其他文件模块导入
from session_control import *
from field_control import *
    
def create_tag(**link_info):
    Tag.objects.get_or_create(username = link_info['username'],tag_name = link_info['link_tag'])

def get_tag_by_username(my_username):
    tag_object_list = Tag.objects.all().filter(username = my_username).values()
    tag_list = []
    for tag in tag_object_list:
        tag_list.append(tag['tag_name'])
    return tag_list


    
