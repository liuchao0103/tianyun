from django.conf.urls import patterns, include, url
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.contrib import admin
from django.views.static import serve as serve_static
from django.views.decorators.cache import never_cache

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.index', name='home'),
    url(r'^login/', include("login.urls")),
    url(r'^logout/', include("logout.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('', url(r'^static/(?P<path>.*)$', never_cache(serve_static),
                                {'document_root': '%s/static' % (settings.PROJECT_ROOT), 'show_indexes': True}))
urlpatterns += patterns('', url(r'^filestorage/(?P<path>.*)$', never_cache(serve_static),
                                {'document_root': '%s' % (settings.PROJECT_ROOT), 'show_indexes': True}))