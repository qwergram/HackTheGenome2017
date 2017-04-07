from django.contrib import admin
from dashboard import models

# Register your models here.


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_pk', 'question_pk', 'answer_str')

    def answer_str(self, obj):
        return str(obj)
    answer_str.short_description = "Answer Model"

    def question_pk(self, obj):
        return str(obj.question.pk)
    question_pk.short_description = "Q#"

    def answer_pk(self, obj):
        return str(obj.pk)
    answer_pk.short_description = "A#"


admin.site.register(models.Question)
admin.site.register(models.Answer, AnswerAdmin)
admin.site.register(models.UserResponse)
admin.site.register(models.FeedBackModel)
admin.site.register(models.DiseaseModel)