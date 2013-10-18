# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
#模板导入
from django.template import Context
from django.template.loader import get_template
#模型导入
from e_link_app.models import *
#异常导入
from django.core.exceptions import ObjectDoesNotExist
#日志导入
import logging
#其他文件模块导入
from session_control import *




def check_field(**link_info):
    logger = logging.getLogger("file_log")
    try:
        Field.objects.get(username = link_info['username'],field_name = link_info['link_field'])
    except ObjectDoesNotExist:
        if link_info['link_parent'] != "empty":
            try:
                Field(username = link_info['username'],field_name = link_info['link_parent'])
            except ObjectDoesNotExist:
                logger.error("in check_field function.field parent not exist")
                return False     
        try:
            insert_field = Field(username = link_info['username'],field_name = link_info['link_field'],parent_name = link_info['link_parent'])
            insert_field.save()    
        except Exception:
            logger.error("in check_field function.create field fail")
            return False
    return True

def get_field_by_username(my_username):
    field_object_list = Field.objects.all().filter(username = my_username).values()
    field_list = []
    for field in field_object_list:
        field_list.append(field['field_name'])
    return field_list
