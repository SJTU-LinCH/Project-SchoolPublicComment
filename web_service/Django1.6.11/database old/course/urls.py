#_*_coding:utf-8_*_
from django.conf.urls import patterns, url,include
#导入routers方法
from course import views
from rest_framework import routers

#这个是rest_framework封装django 的routers
router = routers.DefaultRouter()
#注册一下，然后关联后面视图
router.register(r'courses', views.CourseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#注意看这里 ：url(r'^', include(router.urls))
#所有以localhost/api 开头的都去找router.urls
#
urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('router.urls', namespace='rest_framework')
    url(r'^inputcourse/$',views.inputcourse,name = 'inputcourse'),
]
