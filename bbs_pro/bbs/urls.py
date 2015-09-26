from django.conf.urls import patterns, include, url


urlpatterns = patterns('bbs.views',
    # Examples:
    # url(r'^$', 'bbs_pro.views.home', name='home'),
    url(r'^$','index'),
    url(r'^detail/(\d+)/$','detail'),
    url(r'^sub_comment/$','sub_comment'),
)
