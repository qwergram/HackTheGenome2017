from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from dashboard import models, forms
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

class AnswerQuestionsView(TemplateView):
    template_name = "dashboard/_questions.html"

    def get_context_data(self, **kwargs):
        context = super(AnswerQuestionsView, self).get_context_data(**kwargs)
        questionJson = []
        for question in models.Question.objects.all():
            questionJson.append({
                "pk": question.pk,
                "text": str(question),
                "choices": [
                    {
                        "text": answer.answer,
                        "pk": answer.pk
                    } for answer in question.answers.all()
                ]
            })
        context['questionJson'] = questionJson
        return context
        

class HandleAnswersView(View):
    template_name = "dashboard/_questions.html"

    def post(self, request, *args, **kwargs):
        
        contactForm = forms.ContactForm(request.POST)
        genomeForm = forms.GenomeForm(request.POST)
        questionForm = forms.BasicQuestionaire(request.POST)

        print(request.POST)

        # import pdb; pdb.set_trace()

        return render(request, self.template_name, {})

        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})