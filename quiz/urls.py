from django.conf.urls import patterns, url
from quiz import views

urlpatterns = patterns('',
    url(r'^quiz/', views.index, name='index'),
    url(r'^login/', 'quiz.views.login_user'),
)