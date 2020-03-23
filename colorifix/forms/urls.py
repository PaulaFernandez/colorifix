from django.conf.urls import url

from . import views

app_name = 'forms'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.index, name='index'),
    url(r'^save_form/([0-9]+)/$', views.save_form, name='save_form'),
]