from django.urls import path

from . import views

"""
/
/login/
/signup/
/question/<123>/    # вместо <123> - произвольный ID
/ask/
/popular/
/new/
"""

urlpatterns = [
    path(r'^$', views.test, name='test'),
    path(r'^question/[0-9]+/$', views.test, name='test'),
    path(r'^ask/$', views.test, name='test'),
    path(r'^popular/$', views.test, name='test'),
    path(r'^new/$', views.test, name='test'),
]
