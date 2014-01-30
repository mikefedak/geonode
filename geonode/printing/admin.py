#Need to change these locations to point to a non-contrib setup
from geonode.printing.models import PrintTemplate
from django.contrib import admin

admin.site.register(PrintTemplate)
