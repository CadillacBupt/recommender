# -*- coding:utf-8 -*-

#导入模型（包括从e_link_app数据库中导入)
import sys
sys.path.append('/home/lin/web_server/web')

from e_link_app.models import *
from user_base_recommender.models import *
# 导入异常模块
from django.core.exception import ObjectDoesNotExist

#初始化该应用的数据库。
def init_database():
    #首先清空表中数据（因为数据库可能过时了)
    Url.objects.all().delete()
    TopUrl.objects.all().delete()
    #从其他表中获取用户链接信息，并用于初始化数据库
    users = User.objects.all()
    for user in users:
        user_name = user.values()['name']
        links = Link.objects.all().filter(username = user_name)
        for link in links:
            url = Url(username = user_name,link_url = link,click_num = 0)
            url.save()
            top_link = get_top_link(link)
            update_top_url(user_name,top_link)

#返回顶级域名
def get_top_link(link):
    return top_link
#更新顶级域名
def update_top_url(user_name,top_link):
    try:
       url = TopUrl.objects.get(username = user_name,top_url = top_link)        
       url.num += 1
       url.save()
    except ObjectDoesNotExist:
	top_url = TopUrl(username = user_name,top_url = top_link,num = 1)
        top_url.save() 





    
