from django.conf.urls import patterns, url
from quiz import views

urlpatterns = patterns('',
	url(r'^quiz/', views.index, name='index'),
    url(r'^login/', 'quiz.views.login_user'),
    url(r'^signup/', 'quiz.views.signup_user'),
    url(r'^debug/','quiz.views.debug_view'),
    url(r'^user/$', views.userPage, name='user'),
    url(r'^search/$', views.search, name='search'),
    url(r'^createSet/', views.set_create, name='quiz.views.set_create'),
    url(r'^createSetForm/', views.create_set_form, name='quiz.views.create_set_form'),
    url(r'^set/create/', views.set_create, name='set_create'),


    url(r'^set/view/(?P<set_id>\d+)/$', views.get_set, name='get_set'),

    url(r'^dashboard/', views.return_to_dashboard, name='quiz.views.return_to_dashboard'),
    url(r'^editSetForm/(?P<set_id>\d+)/$', views.edit_set_form, name="quiz.views.edit_set_form"),
    url(r'^editSet/', views.edit_set, name='quiz.views.edit_set'),

)