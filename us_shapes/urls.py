from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from geojson_tiles.views import GeoJSONTile
from us_shapes.models import US_State
from us_shapes import views

urlpatterns = patterns('',
    url(r'^states/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).json$', 
        GeoJSONTile(US_State, 'geom', trim_to_boundary=True)
    ),
    url(r'^$', views.map),
)

# static file serving for development. only works when DEBUG=True
urlpatterns += staticfiles_urlpatterns()
