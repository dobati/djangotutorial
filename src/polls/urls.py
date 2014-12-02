from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index', name='index'),
#    url(r'^general2/$', 'polls.views.general2', name='general2'),
)
