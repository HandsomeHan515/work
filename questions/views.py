from rest_framework import viewsets
from rest_framework.decorators import list_route
from .models import Question
from .serializers import QuestionSerializer, QuestionListSerializer


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


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        return PageResponse(self, queryset, QuestionListSerializer)

    @list_route(methods=['POST'])
    def search(self, request):
        keyword = request.data['keyword']
        queryset = self.get_queryset().filter(name__contains=keyword)
        return PageResponse(self, queryset, QuestionListSerializer)
