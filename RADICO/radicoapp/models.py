from django.db import models

# Create your models here.
class startups(models.Model):
    startup_no=models.IntegerField()
    startup_name=models.CharField(max_length=25)
    startup_domain=models.CharField(max_length=28)
    startup_city=models.CharField(max_length=10)

