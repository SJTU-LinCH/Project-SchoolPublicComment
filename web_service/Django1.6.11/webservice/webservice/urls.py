from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.contrib import admin
from rest_framework.response import Response
from item import views
admin.autodiscover()

@api_view(['GET'])
def api_root(request):
    return Response({
        'entertainment': reverse('funlist', request=request),
	'course':  reverse('courselist', request=request),
	'merchant': reverse('merchantlist', request=request),
    })

urlpatterns = [
    url(r'^$',api_root),
    url(r'^course/$', views.CourseList.as_view(),name='courselist'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(),name='coursedetail'),
    url(r'^merchant/$', views.MerchantList.as_view(),name='merchantlist'),
    url(r'^merchant/(?P<pk>[0-9]+)/$', views.MerchantDetail.as_view(),name='merchantdetail'),
    url(r'^fun/$', views.FunList.as_view(),name='funlist'),
    url(r'^fun/(?P<pk>[0-9]+)/$', views.FunDetail.as_view(),name='fundetail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^admin/',include(admin.site.urls)),
]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)
REST_FRAMEWORK={  'PAGE_SIZE' : 5 }
