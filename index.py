import pandas as pd
from shapely.geometry import Point, shape
import geojson
import osmnx as ox
import geopandas as gpd
import json



def containsMunicipality(municipality="barcrelona", lng=2.193568585214233, lat= 41.39758411150723):
    # Get place boundary related to the place name as a geodataframe
    area = ox.geocode_to_gdf(municipality)
    boundaries_json = json.loads(area.to_json())
    #print(type(boundaries_json))
    point = Point(lng,lat)
    contains = shape(boundaries_json["features"][0]["geometry"]).contains(point)
    return contains
