from django.conf.urls import url
from foodapp import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^bmap', views.bmap),
    url(r'^bigdata', views.bigdata),
    url(r'^word_cloud', views.word_cloud),
    url(r'^get_cloud_data', views.get_cloud_data),
    url(r'^get_pie_data', views.get_pie_data),
    url(r'^post/$', views.post),
    url(r'^get_hotmap', views.get_hotmap),
    url(r'^get_form/$', views.get_form),
    url(r'^get_type/$', views.get_type),
    url(r'^get_province/$', views.get_province),
    url(r'^area2/$', views.area2),
    url(r'^area3_(\d+)/$', views.area3),
    url(r'pie_map', views.pie_map),
    url(r'get_detail', views.get_detail),
    url(r'data_detail', views.data_detail),
]