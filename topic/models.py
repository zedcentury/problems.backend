from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
