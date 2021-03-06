from rest_framework import serializers
from .models import Job, JobLevelOne, JobLevelTwo, JobAblityShip
from ablitys.serializers import AblityListSerializer


class JobSerializer(serializers.ModelSerializer):
    ablitys = AblityListSerializer(many=True)
    level_one = serializers.CharField()
    level_two = serializers.StringRelatedField()

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


class JobListSerializer(serializers.ModelSerializer):
    level_one = serializers.CharField()
    level_two = serializers.StringRelatedField()
    ablity = serializers.IntegerField()
    question = serializers.IntegerField()

    class Meta:
        model = Job
        exclude = ('ablitys',)
