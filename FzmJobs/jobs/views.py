from datetime import datetime, timedelta
from typing import List

from rest_framework import views
from rest_framework.renderers import JSONRenderer

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import JobApplication
from .serializers import JobSerializer
from .services import compute_status, compute_application_funnel_dict

# Create your views here.
class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobSerializer

class DashboardView(views.APIView):
    def get(self, request, format=None):
        return Response({
            'status': compute_status(),
            'funnel': compute_application_funnel_dict(),
        })
