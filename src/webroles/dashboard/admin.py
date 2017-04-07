from django.contrib import admin
from dashboard import models

# Register your models here.

admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.UserResponse)
admin.site.register(models.FeedBackModel)