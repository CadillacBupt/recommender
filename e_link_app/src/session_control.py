# -!- coding:utf-8 -!-

#模型导入
from e_link_app.models import *
#异常导入
from django.core.exceptions import ObjectDoesNotExist
#日志导入
import logging
#其他文件模块导入
from session_control import *
from field_control import *



def del_session(request):
    del request.session['username']
    del request.session['email']
    del request.session['authorized']

def add_session(request,username,email):
    request.session['authorized'] = True
    request.session['username'] = username
    request.session['email'] = email

def check_session(request):
    if 'authorized' in request.session and 'username' in request.session and 'email' in request.session:
        try:
            User.objects.get(name = request.session['username'],email = request.session['email'])
            return True
        except ObjectDoesNotExist:
            return False
    else:
        return False
  
