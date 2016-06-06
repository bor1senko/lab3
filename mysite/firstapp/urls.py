from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app/', views.index2, name='index2'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$',views.search),
    url(r'^add-index/$',views.add_index),
    url(r'^info([0-9]+)$',views.info),
    url(r'^save([0-9]+)$',views.add_index),
]
