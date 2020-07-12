from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Job(models.Model):
    date = models.DateTimeField(auto_now=True)
    desription = models.TextField(max_length = 500, null = True)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.userId.username+"JobNo-"+str(self.id)



class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
   #  belong_to = models.ManyToManyField('Category', related_name='services')
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Job_Service(models.Model):
    serviceId = models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    jobId = models.ForeignKey(Job,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.id)
