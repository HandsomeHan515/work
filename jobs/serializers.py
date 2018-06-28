from rest_framework import serializers
from .models import Job, JobLevelOne, JobLevelTwo


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class JobLevelOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobLevelOne
        fields = '__all__'


class JobLevelTwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobLevelTwo
        fields = '__all__'
