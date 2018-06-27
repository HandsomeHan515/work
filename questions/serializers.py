from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    ablity = serializers.StringRelatedField()

    class Meta:
        model = Question
        fields = '__all__'
