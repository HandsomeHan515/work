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

    class Meta:
        model = Ablity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AblitySerializer, self).__init__(*args, **kwargs)

        request = kwargs['context']['request']
        if request.method == 'GET':
            self.fields['level_one'] = serializers.IntegerField()


class AblityListSerializer(serializers.ModelSerializer):
    level_two = serializers.StringRelatedField()
    question = serializers.IntegerField()
    job = serializers.IntegerField()

    class Meta:
        model = Ablity
        fields = "__all__"
