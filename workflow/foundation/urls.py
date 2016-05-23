from django.conf.urls import url, patterns
from .controllers import HeadEnterpriseInstall, EnterpriseView

urlpatterns = patterns('foundation.views',
                       # url(r'^enterprise/$', 'enterprise', name='enterprise'),
                       url(r'^enterprise/create_main', 'create_main_enterprise', name='create_main_enterprise'),
                       url(r'^enterprise/create_branch', 'create_enterprise_branch', name='create_enterprise_branch'),
                       url(r'^enterprise/install/$', HeadEnterpriseInstall.as_view(), name='enterprise_install'),
                       url(r'^enterprise/$', EnterpriseView.as_view(), name='enterprise')
                       )
