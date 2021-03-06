"""sequencehack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dashboard import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # primitive API
    url(r'^api/v1/questions', views.QuestionAPI.as_view()),
    url(r'^api/v1/userResponse', views.QuestionaireAPI.as_view()),

    # chain API
    url(r'^api/v1/skin', views.SkinCancerRiskView.as_view()),
    url(r'^api/v1/liver', views.LiverCancerRiskView.as_view()), # app chain doesn't work!
    url(r'^api/v1/prostate', views.ProstateCancerRiskView.as_view()),
    
    # homepage
    url(r'^$', views.SplashPage.as_view()),

    # user pages
    url(r'^questions/', views.AnswerQuestionsView.as_view()),
    url(r'^submit/$', views.HandleAnswersView.as_view()), # Submission endpoint
    url(r'^dashboard/$', views.DashboardView.as_view())
    # ... Need endpoints for various APIs
]
