import time

from rest_framework.generics import ListAPIView

from topic.models import Topic
from topic.serializers import TopicListSerializer


class TopicListView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer
    pagination_class = None
