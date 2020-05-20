from django.db import models

# Create your models here.
class Emp(models.Model):
    eid=models.IntegerField()
    ename = models.CharField(max_length=5)
    eemail = models.EmailField()
    ephnone_no = models.CharField(max_length=15)