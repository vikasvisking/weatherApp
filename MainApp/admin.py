from django.contrib import admin
from MainApp.models import *

# Register your models here.

# add models to admin pannel
admin.site.register(Metrics)
admin.site.register(MetricsValues)
