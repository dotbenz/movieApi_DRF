from django.contrib import admin
from .models import Movie
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Movie, ImportExportModelAdmin)
