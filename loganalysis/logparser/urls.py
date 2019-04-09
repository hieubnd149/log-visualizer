from django.urls import path 
from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .auth.views import login_func, signup_func, post_logout
from .accesslog import views as accesslog_views

app_name = 'logparser'
urlpatterns = [
    path('', login_func, name='index'),
    url('dashboard', views.index_view, name='dashboard'),
    url('auth/login', login_func, name='auth-login'),
    url('auth/signup', signup_func, name='auth-signup'),
    url('auth/logout', post_logout, name='auth-logout'),

    url('admin', views.adminPage, name='admin-page'),
    url('accesslog/view', accesslog_views.processAccessLog, name='accesslog-view'),
    url('songs', views.get_all_song_view, name='song-all'),
    url('songs_test', views.GetSongView.as_view({'get': 'list'}), name='song-all-test'),
]

urlpatterns = format_suffix_patterns(urlpatterns)