from django.conf.urls import patterns,include,url
from django.contrib import admin
from  login import  urls
from login.views import index
from  course import  urls
from course import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'database.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
    url(r'^course/', include('course.urls')),
    url(r'^api/',include(urls)),
    url(r'^$',index,name="dashboard"),
)
