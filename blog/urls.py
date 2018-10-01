from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^image/$', views.image),
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>\d+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]
