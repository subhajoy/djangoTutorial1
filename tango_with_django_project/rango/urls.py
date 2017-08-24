from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index1, name='index1'),
    url(r'^about/', views.about, name='about')
]