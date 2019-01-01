from django.urls import path 
from django.conf.urls import url 
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .accesslog import views as accesslog_views
from .views import CreateView

app_name = 'logparser'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    url('questions/', CreateView.as_view(), name="create"),
    url('admin/', views.adminPage, name='admin-page'),
    url('logview/', views.logView, name='logview'),

    url('accesslog/view', accesslog_views.processAccessLog, name='accesslog-view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)