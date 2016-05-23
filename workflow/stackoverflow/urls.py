from django.conf.urls import url, patterns

from .views import QuestionsIndex

urlpatterns = patterns('',
    url(r'^questions/$', QuestionsIndex.as_view(), name='questions'),
)