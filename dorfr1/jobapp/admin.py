from django.contrib import admin
from jobapp.models import Job, Service, Job_Service

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['id', 'date', 'desription', 'userId']  

admin.site.register(Job, JobAdmin)

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['name', 'description', 'rate']  

admin.site.register(Service, ServiceAdmin)


class Job_ServiceAdmin(admin.ModelAdmin):
    model = Job_Service
    list_display = ['id', 'serviceId', 'jobId']

admin.site.register(Job_Service, Job_ServiceAdmin)