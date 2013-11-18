from django.conf.urls import patterns, include, url
from django.contrib import admin
from ecoCars.settings import STATIC_ROOT
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^$', include('tabs.urls')),
    #url(r'^admin/', include('admin.site.urls')),
)

urlpatterns += patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : True}),
)
