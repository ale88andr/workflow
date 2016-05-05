from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('documents.views',
    url(r'^resolutions/$', 'resolutions', name='resolutions'),
    url(r'^resolutions/create/', 'create_resolution', name='create_resolution'),
    url(r'^resolutions/(?P<resolution_id>\d+)/delete/', 'delete_resolution', name='delete_resolution'),
    url(r'^incoming/$', 'incoming', name='incoming'),
    url(r'^outbound/$', 'outbound', name='outbound'),
    url(r'^$', 'index', name='documents'),
)