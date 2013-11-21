from tabs.models import GasRate, GasolineCarCount, CompanyWiseCarCount, Mileage, CarCount
from django.contrib import admin

from django.conf.urls import patterns, include, url
admin.autodiscover()
urlpatterns = patterns('',url(r'^admin/', include(admin.site.urls)),)
admin.site.register(GasRate)
admin.site.register(GasolineCarCount)
admin.site.register(CompanyWiseCarCount)
admin.site.register(Mileage)
admin.site.register(CarCount)
