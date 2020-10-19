from import_export import resources

from main.models import JobList


class JoblistResource(resources.ModelResource):
    class Meta:
        model = JobList
