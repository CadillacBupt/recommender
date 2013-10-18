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
from tag_control import *
from pprint import pprint

def add_link(**link_info):
    import pdb
    pdb.set_trace()

    def new_url(url):
        import re
        result = re.search('^http://',url)
        if result is None:
            return 'http://'+url
        else:
            return url

    logger = logging.getLogger("file_log")

    link_info['link_url'] = new_url(link_info['link_url'])

    try: 
        Link.objects.get(username = link_info['username'],link_url = link_info['link_url'])
        
        logger.error("in add_link function.link exist")
        return False
    except ObjectDoesNotExist:
        pass
    
    if check_field(**link_info) == True:
        user_link = Link(link_url = link_info['link_url'],username = link_info['username'],link_name = link_info['link_name'],link_tag = link_info['link_tag'],link_field = link_info['link_field'],like_num = 0,dislike_num = 0,used_num = 0)
        user_link.save() 
        create_tag(**link_info)
    return True

#获取满足条件的链接
def get_link(condtion,kind):
    import pdb
    pdb.set_trace()
    link_array = []
    link_list = {}
    def add_info(link):
        link_map = {}.fromkeys(['id','url','name','tag','field','like_num','dislike_num','used_num'])
        link_map['id'] = link['id']
        link_map['url'] = link['link_url']
        link_map['name'] = link['link_name']
        link_map['tag'] = link['link_tag']
        link_map['field'] = link['link_field']
        link_map['like_num'] = link['like_num']
        link_map['dislike_num'] = link['dislike_num']
        link_map['used_num'] = link['used_num']
        
        link_array.append(link_map)

    if kind == "username":
        link_list = Link.objects.all().filter(username = condtion)
    if kind == "tag":
        link_list = Link.objects.all().filter(link_tag = condtion)
    if kind == "field":
        link_list = Link.objtects.all().filter(link_field = condtion)

    if link_list == {}:
        return False
    else:
        my_link_list = link_list.values()
        for link in my_link_list:
            add_info(link)
        return link_array



def modify_link(request):
    #修改链接。
    pass
def reused_link():
    pass

