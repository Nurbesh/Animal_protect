from django.db import models


class Comment(models.Model):
    animal = models.ForeignKey('animal.Animal', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()


