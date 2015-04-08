from django.conf.urls import patterns, url
from quiz import views

urlpatterns = patterns('',
	url(r'^quiz/', views.index, name='index'),
    url(r'^login/', 'quiz.views.login_user'),
    url(r'^signup/', 'quiz.views.signup_user'),
    url(r'^debug/','quiz.views.debug_view'),
    url(r'^user/$', views.userPage, name='user'),
    url(r'^search/$', views.search, name='search'),
    url(r'^set/create/', views.set_create, name='set_create'),
)