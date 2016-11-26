#_*_coding:utf-8_*_
from django.conf.urls import patterns,include,url
from django.contrib import admin
import  login.urls
import login.views
import  course.urls
import course.views
import  merchant.urls
import merchant.views
import  entertainment.urls
import entertainment.views
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', include(login.urls), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include(login.urls)),
    url(r'^course/', include(course.urls)),
    url(r'^merchant/', include(merchant.urls)),
    url(r'^entertainment/', include(entertainment.urls)),
    url(r'^api/',include(login.urls)),

)
