from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<series_number>[0-9]+)/$', views.series_details, name='details')
]