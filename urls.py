from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'rss_duna.feed.views.home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #(r'^feed/$', DunaEntriesFeed()),
    (r'^duna/(?P<programa_id>\D+)/rss/$', 'rss_duna.feed.views.get_feed_rss'),
    (r'^duna/feeds/$', 'rss_duna.feed.views.list_feeds'),
    #(r'^prueba/$', 'rss_duna.feed.views.prueba')
)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':False}),
#    )

