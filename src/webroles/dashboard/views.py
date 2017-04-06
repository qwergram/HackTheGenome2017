from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from dashboard import models
import json


class QuestionAPI(View):
    
    # TODO: Replace this with an actual API implementation
    def get(self, request):
        return_blob = {}
        for question in models.Question.objects.all():
            return_blob[question.pk] = {
                "question": str(question),
                "answers": [_.answer for _ in question.answers.all()]
            }
        return HttpResponse(json.dumps(return_blob, indent=2))


class SplashPage(TemplateView):
    template_name = "dashboard/splash.html"

class AnswerQuestionsView(View):

    def get(self, request):
        pass