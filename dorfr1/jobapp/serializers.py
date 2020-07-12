from rest_framework import serializers
from jobapp.models import Job, Service, Job_Service


class jobSerializer(serializers.ModelSerializer):
    userId = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Job
        fields = ['id', 'date', 'desription', 'userId']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'rate']


class Job_ServiceSerializer(serializers.ModelSerializer):
    serviceId = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Job_Service
        fields = ['id', 'serviceId', 'jobId']