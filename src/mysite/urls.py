# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'polls.views.index', name='index'),
    url(r'^about_us/$', 'polls.views.about_us', name='about_us'),
    url(r'^about_ve/$', 'polls.views.about_ve', name='about_ve'),
    url(r'^general1/$', 'polls.views.general1', name='general1'),
    url(r'^general2/$', 'polls.views.general2', name='general2'),
    url(r'^general3/$', 'polls.views.general3', name='general3'),
    url(r'^translate/$', 'polls.views.books1', name='translate'),
    url(r'^books2/$', 'polls.views.books2', name='books2'),
    url(r'^books3/$', 'polls.views.books3', name='books3'),
    url(r'^movies1/$', 'polls.views.movies1', name='movies1'),
    url(r'^movies2/$', 'polls.views.movies2', name='movies2'),
    url(r'^movies3/$', 'polls.views.movies3', name='movies3'),
    url(r'^legaltexts1/$', 'polls.views.legaltexts1', name='legaltexts1'),
    url(r'^legaltexts2/$', 'polls.views.legaltexts2', name='legaltexts2'),
    url(r'^legaltexts3/$', 'polls.views.legaltexts3', name='legaltexts3'),
    
    
    url(r'^admin/', include(admin.site.urls)),
)


###from django.conf.urls import patterns, include, url
###from django.contrib import admin
###
###urlpatterns = patterns('',
###    url(r'^admin/', include(admin.site.urls)),
###    url(r'', include('polls.urls')),
###)
