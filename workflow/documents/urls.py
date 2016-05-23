from django.conf.urls import url, patterns
from .controllers import ResolutionsController, DeleteResolution

urlpatterns = patterns('documents.views',
                       url(r'^resolutions/$', ResolutionsController.as_view(), name='resolutions'),
                       url(r'^resolutions/(?P<pk>\d+)/delete/', DeleteResolution.as_view(), name='delete_resolution'),
                       url(r'^incoming/$', 'incoming', name='incoming'),
                       url(r'^outbound/$', 'outbound', name='outbound'),
                       url(r'^$', 'index', name='documents'),
                       )
