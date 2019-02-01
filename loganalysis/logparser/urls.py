from django.urls import path 
from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .auth.views import LoginView, signup
from .accesslog import views as accesslog_views

app_name = 'logparser'
urlpatterns = [
    # path('', views.index, name='index'),
    url('auth/login', LoginView.as_view(), name='auth-login'),
    url('auth/signup', signup, name='auth-signup'),

    url('admin', views.adminPage, name='admin-page'),
    url('accesslog/view', accesslog_views.processAccessLog, name='accesslog-view'),
    url('songs', views.get_all_song_view, name='song-all'),
]

urlpatterns = format_suffix_patterns(urlpatterns)