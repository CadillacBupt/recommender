#-*-coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from e_link_app.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
media = 'e_link_app/html/media'

urlpatterns = patterns('',
#登陆相关
(r'^$',main),#首页
(r'^authorize/$',authorize),#认证
(r'^login/$',login),#登陆
(r'^regist/$',regist),#注册
(r'^logout/$',logout),#登出
#静态文件相关
(r'media/(?P<path>.*)$','django.views.static.serve',{'document_root':media}),
#用户主页
(r'^user/$',user_page),#跳转到用户主页
(r'^user/add_link/$',user_link_add),#用户提交表单

)

    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),

    #Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
