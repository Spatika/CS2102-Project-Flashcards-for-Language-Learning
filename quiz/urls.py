from django.conf.urls import patterns, url
from quiz import views

urlpatterns = patterns('',
	url(r'^quiz/', views.index, name='index'),
    url(r'^login/', 'quiz.views.login_user'),
    url(r'^signup/', 'quiz.views.signup_user'),
    url(r'^debug/','quiz.views.debug_view'),
    url(r'^user/$', views.userPage, name='user'),

    # url(r'^user/(?P<user_id>\d+)/$', views.users, name='account'),
    url(r'^search/$', views.search, name='search'),
    # url(r'^search/(?P<user_name>[\w\s.])/$', views.search, name='search'),
    url(r'^set/create/', views.set_create, name='set_create'),

    url(r'^set/view/(?P<set_id>\d+)/$', views.get_set, name='get_set'),
)