from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from problem.models import Problem
from problem.serializers import ProblemListSerializer


class ProblemListView(ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['topic']
    search_fields = ['content']
