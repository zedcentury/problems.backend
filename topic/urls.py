from django.urls import path

from topic.views import TopicListView

urlpatterns = [
    path('list/', TopicListView.as_view(), name='topic-list')
]
