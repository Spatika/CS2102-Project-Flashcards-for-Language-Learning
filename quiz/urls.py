from django.conf.urls import patterns, url
from quiz import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^user/$', views.userPage, name='user'),
    url(r'^search/$', views.search, name='search'),
    # url(r'^search/(?P<user_id>[\w\s.]+)/$', views.search, name='search'),
)