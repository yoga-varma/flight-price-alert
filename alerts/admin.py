from django.contrib import admin
from .models import Route, Alert, PriceSnapshot

admin.site.register(Route)
admin.site.register(Alert)
admin.site.register(PriceSnapshot)