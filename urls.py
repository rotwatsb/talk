from django.conf.urls import url

from . import views

app_name = 'talk'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^block/(?P<block_hash>[0-9a-f]+)/$', views.block_detail, name='block_detail'),
    url(r'^transaction/(?P<tx_hash>[0-9a-f]+)/$', views.transaction_detail, name='transaction_detail'),
    url(r'^block/(?P<block_hash>[0-9a-f]+)/post/$', views.block_post, name='block_post'),
]
