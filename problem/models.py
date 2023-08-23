from django.db import models

from topic.models import Topic


class Problem(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.RESTRICT)
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
