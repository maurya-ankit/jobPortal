from django.contrib.auth.models import User
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


class FillUpForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uniq_id = models.ForeignKey(JobList, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=63)
    lastName = models.CharField(max_length=63)
    email = models.EmailField()
    city=models.CharField(max_length=63)
    state=models.CharField(max_length=63)
    pincode=models.CharField(max_length=15)
    Resume = models.FileField(upload_to='upload/resume/')