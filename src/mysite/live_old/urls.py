# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.index', name='index'),
    url(r'^about_us/$', 'views.about_us', name='about_us'),
    url(r'^about_ve/$', 'views.about_ve', name='about_ve'),
    url(r'^general1/$', 'views.general1', name='general1'),
    url(r'^general2/$', 'views.general2', name='general2'),
    url(r'^general3/$', 'views.general3', name='general3'),
    url(r'^translate/$', 'views.books1', name='translate'),
    url(r'^books2/$', 'views.books2', name='books2'),
    url(r'^books3/$', 'views.books3', name='books3'),
    url(r'^movies1/$', 'views.movies1', name='movies1'),
    url(r'^movies2/$', 'views.movies2', name='movies2'),
    url(r'^movies3/$', 'views.movies3', name='movies3'),
    url(r'^legaltexts1/$', 'views.legaltexts1', name='legaltexts1'),
    url(r'^legaltexts2/$', 'views.legaltexts2', name='legaltexts2'),
    url(r'^legaltexts3/$', 'views.legaltexts3', name='legaltexts3'),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^polls/', include('polls.urls')),
)
