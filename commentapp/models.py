from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    comment_body = models.CharField(max_length=1000)
    date_published = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.comment_body

class Commenter(models.Model):
    commener_body = models.CharField(max_length=200)
    