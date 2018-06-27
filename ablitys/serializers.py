from rest_framework import serializers
from .models import Ablity, AblityLevelOne, AblityLevelTwo


class AblityLevelOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = AblityLevelOne
        fields = "__all__"


class AblityLevelTwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AblityLevelTwo
        fields = "__all__"


class AblitySerializer(serializers.ModelSerializer):
    level_one = serializers.IntegerField()

    class Meta:
        model = Ablity
        fields = "__all__"


class AblityListSerializer(serializers.ModelSerializer):
    level_two = serializers.StringRelatedField()

    class Meta:
        model = Ablity
        fields = "__all__"
