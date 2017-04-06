from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.


class TimeStampMixin(object):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class JsonResultMixin(object):
    result = models.TextField()

    @property
    def resultJson(self):
        return json.loads(result.to_python)


class Question(models.Model, TimeStampMixin):
    question = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.question


class Answer(models.Model, TimeStampMixin):
    answer = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name="answers")

    def __str__(self):
        return str(self.question) + ": " + str(self.answer)

class UserResponse(models.Model, TimeStampMixin, JsonResultMixin):
    user = models.ForeignKey(User, related_name="responses")
    
    def similarity(self, diseaseModel):
        return 0


class _DiseaseModel(models.Model, TimeStampMixin, JsonResultMixin):
    name = models.CharField(unique=True, max_length=255)

    def similarity(self, userResponseModel):
        return 0