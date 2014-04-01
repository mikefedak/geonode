from django.contrib.gis import admin
from models import Shelter_Details as SDtl 

admin.site.register(SDtl, admin.GeoModelAdmin) 
