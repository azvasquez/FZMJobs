from jobs.models import JobApplication
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'