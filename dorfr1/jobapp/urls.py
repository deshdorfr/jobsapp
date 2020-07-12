from django.contrib import admin
from django.urls import path
from jobapp import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin' ),
    path('jobs/', views.job_list, name = 'job_list'),
    path('jobs/<int:pk>/', views.job_detail),
    path('services/', views.service_list, name = 'service_list'),
    path('services/<int:pk>/', views.service_detail),
    path('jobservices/', views.Job_Service_list, name = 'Job_Service_list'),
    path('jobservices/<int:pk>/', views.Job_Service_detail),
]
