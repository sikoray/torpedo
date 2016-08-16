from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.contact, name='contact'),
    url(r'^contact/$', views.contact, name='contact'),
	]