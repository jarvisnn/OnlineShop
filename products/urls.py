from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>[0-9]+)/$', views.getProduct, name='getProduct'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.getProductWithCategory, name='getProductWithCategory'),
    url(r'^search/$', views.search, name='search'),
]
