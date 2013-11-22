from django.conf.urls import patterns, include, url
from django.contrib import admin
from ecoCars.settings import STATIC_ROOT
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tabs.views.home', name='home'),
    url(r'^count/', 'tabs.views.count', name='count'),
    url(r'^companies/', 'tabs.views.companies', name='companies'),
    url(r'^advantages/', 'tabs.views.advantages', name='advantages'),
    url(r'^mileage/', 'tabs.views.mileage', name='mileage'),
    url(r'^demand/', 'tabs.views.demand', name='demand'),
    url(r'^saved/', 'tabs.views.saved', name='saved'),
    url(r'^sources/', 'tabs.views.sources', name='sources'),
    url(r'^twitter/', 'tabs.views.twitter', name='twitter'),
    url(r'^calculator/', 'tabs.views.calculator', name='calculator'),
    url(r'^calculated/', 'tabs.views.calculator', name='savings'),
    url(r'^about/', 'tabs.views.about', name='about'),
    url(r'^stations/', 'tabs.views.stations', name='stations'),
    url(r'^references/', 'tabs.views.references', name='references'),
    #url(r'^admin/', include('admin.site.urls')),
)

urlpatterns += patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : True}),
)
