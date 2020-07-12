from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jobapp.models import Job, Service, Job_Service
from jobapp.serializers import jobSerializer, ServiceSerializer, Job_ServiceSerializer


@api_view(['GET', 'POST'])
def job_list(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = jobSerializer(jobs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = jobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, pk):
    try:
        job_data = Job.objects.get(pk=pk)
    except job_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = jobSerializer(job_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = jobSerializer(job_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for Service Handeller
@api_view(['GET', 'POST'])
def service_list(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk):
    try:
        services_data = Service.objects.get(pk=pk)
    except services_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(services_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializer(services_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        services_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Views for Job_Service Handeller
@api_view(['GET', 'POST'])
def Job_Service_list(request):
    if request.method == 'GET':
        Job_Services = Job_Service.objects.all()
        serializer = Job_ServiceSerializer(Job_Services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Job_ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Job_Service_detail(request, pk):
    try:
        Job_Services = Job_Service.objects.get(pk=pk)
    except Job_Services.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Job_ServiceSerializer(Job_Services)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Job_ServiceSerializer(Job_Services, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Job_Services.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)