from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from dashboard import models, forms
import json

# Include Chains views

from dashboard.chains.skinCancerRisk import SkinCancerRiskView
from dashboard.chains.liverCancerRisk import LiverCancerRiskView
from dashboard.chains.prostateCancerRisk import ProstateCancerRiskView

# Other Views

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
        
# Show a cool loading page
class HandleAnswersView(View):
    template_name = "dashboard/loading.html"

    def get(self, request):
        # Won't actually do anything
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):        
        jsonblob = {}

        contactForm = forms.ContactForm(request.POST)
        genomeForm = forms.GenomeForm(request.POST)
        questionForm = forms.BasicQuestionaire(request.POST)

        if (questionForm.is_valid()):
            try:
                jsonblob = {int(q[1:]): int(a[1:]) for (q, a) in questionForm.questions.items()}
            except ValueError:
                jsonblob = {}

        if (genomeForm.is_valid()):
            print(genomeForm.cleaned_data)

        if (contactForm.is_valid()):
            newFeedBack = models.FeedBackModel(
                name=contactForm.cleaned_data['name'],
                email=contactForm.cleaned_data['email'],
                message=contactForm.cleaned_data['message'],
                subject=contactForm.cleaned_data['subject']
            )
            newFeedBack.save()

        return render(request, self.template_name, {})


class DashboardView(TemplateView):
    template_name = 'dashboard/results.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        
        return context