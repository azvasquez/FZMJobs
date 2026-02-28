from django.shortcuts import render
from rest_framework import viewsets
from .models import JobApplication
from .serializers import JobSerializer

# Create your views here.
class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobSerializer
