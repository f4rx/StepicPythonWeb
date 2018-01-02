from django.conf.urls import url
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
    url(r'^$', views.test,),
    url(r'^login/$', views.test,),
    url(r'^signup/$', views.test,),
    url(r'^question/[0-9]+/$', views.test, ),
    url(r'^ask/$', views.test,),
    url(r'^popular/', views.test,),
    url(r'^new/', views.test,),
]
