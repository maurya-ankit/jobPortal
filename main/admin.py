from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from main.models import JobList, FillUpForm


# Register your models here.
@admin.register(JobList)
class JobListAdmin(ImportExportModelAdmin):
    pass


admin.site.register(FillUpForm)
