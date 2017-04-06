from django.db import models
from django.contrib.auth import User
import json

# Create your models here.


class TimeStampMixin(object):
    date_created = models.TimeDate(auto_now_add=True)
    date_modified = models.TimeDate(auto_now=True)


class JsonResultMixin(object):
    result = models.TextField()

    @property
    def resultJson(self):
        return json.loads(result.to_python)


class Question(models.Model, TimeStampMixin):
    question = models.CharField(unique=True, max_length=255)


class Answer(models.Model, TimeStampMixin):
    answer = models.CharField(max_length=255)
    question = models.ForeignKey(related_name="answers")


class UserResponse(models.Model, TimeStampMixin, JsonResultMixin):
    user = models.ForeignKey(User)
    
    def similarity(self, diseaseModel):
        return 0


class _DiseaseModel(models.Model, TimeStampMixin, JsonResultMixin):
    name = models.CharField(unique=True, max_length=255)

    def similarity(self, userResponseModel):
        return 0