from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs_pro.views.home', name='home'),
    url(r'^', include('bbs.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
   
)

urlpatterns += patterns('bbs_pro.views',
	url(r'^logout/$','Logout'),
	url(r'^acc_login/$','acc_login'),
	url(r'^login/$','Login'),
	)
