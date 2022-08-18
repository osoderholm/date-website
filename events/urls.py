from django.conf.urls import url
from django.urls import path, include
from . import views, feed

app_name = 'events'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    path('baal/', views.baal_home, name='baal'),
    path('100/', views.kk100_index, name='kk100'),
    url(r'^(?P<slug>[-\w]+)/anmalan/$', views.EventDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.EventDetailView.as_view(), name='detail'),
    url(r'^feed$', feed.EventFeed(), name='feed'),
]
