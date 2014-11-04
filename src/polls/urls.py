from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index', name='index'),
  #  url(r'^legaltexts11/$', 'polls.views.legaltexts11', name='legaltexts11')
)
