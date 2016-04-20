from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^incoming/$', 'documents.views.incoming', name='incoming'),
    url(r'^outbound/$', 'documents.views.outbound', name='outbound'),
    url(r'^$', 'documents.views.index', name='documents')
]