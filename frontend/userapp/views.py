from django.shortcuts import render
from django.views.generic import TemplateView

# All page views 
class HomePageView(TemplateView):
    template_name = "homepage.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class RegisterPageView(TemplateView):
    template_name = "register.html"

class AccountPageView(TemplateView):
    template_name = "account.html"

class ChatPageView(TemplateView):
    template_name = "chat.html"

class RecommendationPageView(TemplateView):
    template_name = "recommendation.html"

class MoviePageView(TemplateView):
    template_name = "movie.html"


