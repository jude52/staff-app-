from django.db import models

# Create your models here.
class StaffInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()