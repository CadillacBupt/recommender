# Create your views here.
#-*- coding:utf-8 -*-

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

from e_link_app.models import *

from django.views.decorators.csrf import csrf_exempt

##############其他模块导入########################
from .src.session_control import *
from .src.link_control import *



#############登陆模块############################
#登陆首页面
def main(request):
    #根据session来判断该用户是否已经登陆
    flag = False
    if check_session(request) == True:
        flag = True

    #返回对应的页面
    temp = get_template('main.html')
    html = temp.render(Context({"authorized":flag}))
    return HttpResponse(html)

#认证页面
def authorize(request):
    if check_session(request) == True:
        HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        temp = get_template('user_manage/authorize.html')
        html = temp.render(Context({'login_information':'','regist_information':''}))
        return HttpResponse(html)

#认证页面下的登陆函数
@csrf_exempt
def login(request):
    username = ''
    user_password = ''
    user_email = ''
    temp = get_template('user_manage/authorize.html')

    if 'login_username'in request.POST and 'login_password' in request.POST:
        username = request.POST['login_username']
        user_password = request.POST['login_password']
    else:
        html = temp.render(Context({'login_information':'出现了未知的错误！','regist_information':' '})) 
        return HttpResponse(html)
    
    try:
        user = User.objects.get(name = username,password = user_password)
        user_email = user.email
    except User.DoesNotExist:
        html = temp.render(Context({'login_information':'用户名或者密码出错','regist_information':' '})) 
        return HttpResponse(html)
    #登陆成功则返回用户相应的页面
    #利用session来确认用户已经登陆
  
    add_session(request,username,user_email)
    login_url = 'http://127.0.0.1:8000/user/'
    return HttpResponseRedirect(login_url) 

#认证页面下的注册函数
@csrf_exempt
def regist(request):
    temp = get_template('user_manage/authorize.html')
    regist_username = ''
    regist_password = ''
    regist_email = ''

    #获取用户信息
    if 'regist_username' in request.POST and 'regist_password' in request.POST and 'email' in request.POST:
        regist_username = request.POST['regist_username']
        regist_password = request.POST['regist_password']
        regist_email = request.POST['email']
    else:
        html = temp.render(Context({'login_information':' ','regist_information':'出现了未知的错误！！'}))
        return HttpResponse(html)
    
    try:
        test_username = User.objects.get(name = regist_username)
        html = temp.render(Context({'login_information':' ','regist_information':'用户名已经存在'}))
    except User.DoesNotExist:
        pass;
    
    try:
        test_email = User.objects.get(email = regist_email)
        html = temp.render(Context({'login_information':' ','regist_information':'邮箱已经被注册'}))
    except User.DoesNotExist:
        pass;
    
    #将注册信息存入数据库
    insert_data = User(name = regist_username,password = regist_password,email = regist_email)
    insert_data.save()

    #返回登陆后的页面
   
    add_session(request,regist_username,regist_email)
    
    login_url = 'http://127.0.0.1:8000/user/'
    return HttpResponseRedirect(login_url)


#认证成功后的跳转页面        
def user_page(request):
    if check_session(request):
        link_array = user_link_get(request,request.session['username'],"username")
        if link_array == False:
            link_array = []
        tag_array = get_tag_by_username(request.session['username'])
        field_array = get_field_by_username(request.session['username'])
        return  render_to_response('user_home.html',{'username':request.session['username'],'email':request.session['email'],'tags':tag_array,'fields':field_array,'link_array':link_array})
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/')
#登出页面
def logout(request):
    if check_session(request):    
        del_session(request)
        return HttpResponseRedirect('http://127.0.0.1:8000/')

########个人主页模块######################
@csrf_exempt
def user_link_add(request):
    from pprint import pprint
    pprint("i am in the func")
    if request.session['authorized']== False:
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    link_info = {}
    link_info['link_url'] = request.POST['link_url']
    link_info['username'] = request.session['username']
    link_info['link_name'] = request.POST['link_name']
    link_info['link_tag'] = request.POST['link_tag']
    link_info['link_field'] = request.POST['link_field']
    link_info['link_parent'] = request.POST['link_parent']
    add_link(**link_info)
    return HttpResponseRedirect('http://127.0.0.1:8000/user/')

def user_link_get(request,condition,kind):
    if check_session(request) == False:
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    return get_link(condition,kind)
   
        
   
        
        
