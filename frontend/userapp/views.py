from urllib.parse import urlencode
from django.shortcuts import render
from django.views.generic import TemplateView

# All page views 
class HomePageView(TemplateView):
    template_name = "homepage.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class RegisterPageView(TemplateView):
    template_name = "register.html"

class ProfilePageView(TemplateView):
    template_name = "account.html"

class RecommendationPageView(TemplateView):
    template_name = "recommendation.html"

class HistoryPageView(TemplateView):
    template_name = "history.html"

class MoviePageView(TemplateView):
    template_name = "movie.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_id = kwargs.get('movie_id')
        
        api_base_url = 'http://127.0.0.1:8000/api/v1/movies/'

        if movie_id is not None:
            api_base_url = f'http://127.0.0.1:8000/api/v1/movies/{movie_id}/'
        
        context['api_movie_url'] = api_base_url

        return context


class AdminPageView(TemplateView):
    template_name = "admin.html"


