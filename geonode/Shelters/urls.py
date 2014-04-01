from django.conf.urls import patterns, url, include
from django.contrib.gis import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
