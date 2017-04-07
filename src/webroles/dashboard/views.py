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
        
"""
<QueryDict: {
    'subject': [''], 
    'q4': ['a12'], 
    'message': [''], 
    'email': [''], 
    'file_button': ['on'], 
    'csrfmiddlewaretoken': ['czeH0ah7wR0Huyt7Fzcn4XTgCBt0ZzCTt46LRX1QEY4iuvgY6ypi8JcCnjTEwWpf'], 
    'q2': ['a6'], 'q5': ['a14'], 
    'file': ['237697'], 'q3': ['a8'], 
    'q1': ['a1'], 'name': ['']
}>
"""
class HandleAnswersView(View):
    template_name = "dashboard/_questions.html"

    def post(self, request, *args, **kwargs):        
        jsonblob = {}

        contactForm = forms.ContactForm(request.POST)
        genomeForm = forms.GenomeForm(request.POST)
        questionForm = forms.BasicQuestionaire(request.POST)

        if (questionForm.is_valid()):
            jsonblob = {int(q[1:]): int(a[1:]) for (q, a) in questionForm.questions.items()}

            if (GenomeForm.is_valid()):
                pass

        if (contactForm.is_valid()):
            newFeedBack = models.FeedBackModel(
                name=contactForm.cleaned_data['name'],
                email=contactForm.cleaned_data['email'],
                message=contactForm.cleaned_data['message'],
                subject=contactForm.cleaned_data['subject']
            )
            newFeedBack.save()

        print(request.POST)

        return render(request, self.template_name, {})

        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})