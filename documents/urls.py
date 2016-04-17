from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'documents.views.index', name='documents')
]