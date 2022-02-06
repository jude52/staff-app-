
from django.db import models
from datetime import datetime

# Create your models here.
class StaffInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return "input.html"

    # def filter_by_last_name(self, last_name):
    #     return models.objects.filter(self.last_name=last_name)