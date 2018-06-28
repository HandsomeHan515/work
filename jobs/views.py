from rest_framework import viewsets
from .models import Job, JobLevelOne, JobLevelTwo
from .serializers import JobSerializer, JobLevelOneSerializer, JobLevelTwoSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobLevelOneViewSet(viewsets.ModelViewSet):
    queryset = JobLevelOne.objects.all()
    serializer_class = JobLevelOneSerializer


class JobLevelTwoViewSet(viewsets.ModelViewSet):
    queryset = JobLevelTwo.objects.all()
    serializer_class = JobLevelTwoSerializer
