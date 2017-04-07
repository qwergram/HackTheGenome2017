from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.


class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    question = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.question


class Answer(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    answer = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name="answers")

    def __str__(self):
        return str(self.question) + ": " + str(self.answer)

class UserResponse(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="responses")
    result = models.TextField()

    @property
    def resultJson(self):
        return json.loads(result.to_python)
    
    def similarity(self, diseaseModel):
        return 0


class _DiseaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(unique=True, max_length=255)
    result = models.TextField()

    @property
    def resultJson(self):
        return json.loads(result.to_python)

    def similarity(self, userResponseModel):
        return 0