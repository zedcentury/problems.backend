from django.urls import path

from problem.views import ProblemListView

urlpatterns = [
    path('list/', ProblemListView.as_view(), name='problem-list')
]
