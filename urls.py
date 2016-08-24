from django.conf.urls import url

from . import views

app_name = 'talk'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^block/(?P<block_hash>[0-9a-f]+)/$', views.block_detail, name='block_detail'),
]
