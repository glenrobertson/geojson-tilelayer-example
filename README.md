# US Shapes GeoJSON Tile Layer Demo

Demonstrates an example use of:
1. `django-geojson-tiles` (http://pypi.python.org/pypi/django-geojson-tiles )
1. `L.TileLayer.GeoJSON` (https://github.com/glenrobertson/leaflet-tilelayer-geojson)


## Setup

    pip install -r requirements.txt

Install GeoDjango libraries, and PostgreSQL with PostGIS, and configure settings.py with your db settings

    python manage.py syncdb
    python manage.py loaddata shapefiles/usa_state_shapefile.shp
    gunicorn_django --workers=10

Go to http://localhost:8000/
