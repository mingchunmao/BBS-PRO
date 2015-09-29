from django.conf.urls import patterns, include, url


urlpatterns = patterns('bbs.views',
    # Examples:
    # url(r'^$', 'bbs_pro.views.home', name='home'),
    url(r'^$','index'),
    url(r'^detail/(\d+)/$','detail'),
    url(r'^sub_comment/$','sub_comment'),
    url(r'^bbs_pub/$','bbs_pub'),
    url(r'^bbs_sub/$','bbs_sub'),
    url(r'^categray/(\d+)/$','categray'), 
    url(r'^chat_sub/$','chat_sub'),
    url(r'^chat_pub/$','chat_pub'),
)
