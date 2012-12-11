# US States GeoJSON Tile Demo
An example application that serves GeoJSON tiles using GeoDjango and renders them in Leaflet

## Introduction

This application demonstrates an example use of

1. Serving GeoJSON tiles in Django (using `django-geojson-tiles`)
2. Rendering GeoJSON tiles in Leaflet (using https://github.com/glenrobertson/leaflet-tilelayer-geojson)


## Setup

1. Install PostgreSQL with PostGIS, and configure settings.py with your db settings
2. Setup Django app and run

        pip install -r requirements.txt
        python manage.py syncdb
        python manage.py loaddata shapefiles/usa_state_shapefile.shp
        gunicorn_django --workers=10

3. Go to http://localhost:8000/


## Other
US State shapefiles from: http://geocommons.com/overlays/21424

Code licenced under MIT licence