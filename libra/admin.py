from django.contrib import admin
from .import models
# Register your models here.


admin.site.register(models.Library)
admin.site.register(models.datamember)
admin.site.register(models.Records)