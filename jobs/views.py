from rest_framework import viewsets
from .models import Job, JobLevelOne, JobLevelTwo
from .serializers import JobSerializer, JobLevelOneSerializer, JobLevelTwoSerializer, JobListSerializer


def PageResponse(self, data, serializer_class):
    page = self.paginate_queryset(data)
    if page is not None:
        serialize = serializer_class(
            page,
            many=True,
            context={'request': self.request},
        )
        return self.get_paginated_response(serialize.data)

    serializer = serializer_class(
        data,
        many=True,
        context={'request': self.request},
    )
    return Response(serializer.data)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('id')
    serializer_class = JobSerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        return PageResponse(self, queryset, JobListSerializer)


class JobLevelOneViewSet(viewsets.ModelViewSet):
    queryset = JobLevelOne.objects.all()
    serializer_class = JobLevelOneSerializer


class JobLevelTwoViewSet(viewsets.ModelViewSet):
    queryset = JobLevelTwo.objects.all()
    serializer_class = JobLevelTwoSerializer
