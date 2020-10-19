from django.db import models


# Create your models here.

class JobList(models.Model):
    company = models.TextField()
    education = models.TextField()
    experience = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    jobdescription = models.TextField()
    jobid = models.CharField(max_length=255)
    joblocation_address = models.TextField()
    jobtitle = models.CharField(max_length=255)
    numberofpositions = models.CharField(max_length=255)
    payrate = models.CharField(max_length=255)
    postdate = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    uniq_id = models.CharField(max_length=255)
