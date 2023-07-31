from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

# Create your models here.
class Questions(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=3000)

    def __str__(self) -> str:
        return self.question


class Answers(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    questions = models.ForeignKey(author, on_delete=models.CASCADE)
    answers = models.TextField(max_length=3000)

    def __str__(self):
        return str(self.question)










