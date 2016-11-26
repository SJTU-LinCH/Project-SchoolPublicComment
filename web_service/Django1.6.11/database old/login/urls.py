#_*_coding:utf-8_*_
from django.conf.urls import patterns, url,include
from login import views
from rest_framework import routers
#导入routers方法


#这个是rest_framework封装django 的routers
router = routers.DefaultRouter()
#注册一下，然后关联后面视图
router.register(r'users', views.UserViewSet)
#router.register(r'login', views.LoginViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#注意看这里 ：url(r'^', include(router.urls))
#所有以localhost/api 开头的都去找router.urls
#
urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('router.urls', namespace='rest_framework')
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
]
