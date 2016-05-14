from django.conf.urls import include, url, patterns

urlpatterns = patterns('foundation.views',
    url(r'^enterprise/$', 'enterprise', name='enterprise'),
    url(r'^enterprise/create_main', 'create_main_enterprise', name='create_main_enterprise')
)