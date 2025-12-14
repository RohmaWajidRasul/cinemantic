from urllib.parse import urlencode
from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# All page views 
class HomePageView(TemplateView):
    template_name = "homepage.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class RegisterPageView(TemplateView):
    template_name = "register.html"

class ProfilePageView(TemplateView):
    template_name = "profile.html"

class RecommendationPageView(TemplateView):
    template_name = "recommendation.html"

    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        movie_name = self.request.GET.get('movie-name') 
        movie_id = self.request.GET.get('id')
        
        if movie_name:
            
            api_url = f'http://127.0.0.1:8000/api/v1/movies/?title={movie_name}'

            try:

                response = requests.get(api_url, timeout=10) 
                response.raise_for_status() 
                fetched_data = response.json()
                context['movies'] = fetched_data

            except requests.exceptions.RequestException as e:
                print(f"Error fetching external data: {e}")
    
        elif movie_id: 

            api_url = f'http://127.0.0.1:8000/api/v1/movies/{movie_id}/recommendations/'

            try:

                response = requests.get(api_url, timeout=10) 
                response.raise_for_status() 
                fetched_data = response.json()
                context['recs'] = fetched_data
            
            except requests.exceptions.RequestException as e:
                print(f"Error fetching external data: {e}")

        return context
    
class HistoryPageView(TemplateView):
    template_name = "history.html"

    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        movie_name = self.request.GET.get('movie-name') 
        movie_id = self.request.GET.get('id')
        
        if movie_name:
            
            api_url = f'http://127.0.0.1:8000/api/v1/movies/?title={movie_name}'

            try:

                response = requests.get(api_url, timeout=10) 
                response.raise_for_status() 
                fetched_data = response.json()
                context['movies'] = fetched_data

            except requests.exceptions.RequestException as e:
                print(f"Error fetching external data: {e}")
    
        elif movie_id: 

            api_url = f'http://127.0.0.1:8000/api/v1/movies/{movie_id}/recommendations/'

            try:

                response = requests.get(api_url, timeout=10) 
                response.raise_for_status() 
                fetched_data = response.json()
                context['recs'] = fetched_data
            
            except requests.exceptions.RequestException as e:
                print(f"Error fetching external data: {e}")

        return context

class MoviePageView(TemplateView):
    template_name = "movie.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        movie_id = kwargs.get('movie_id')

        if movie_id is not None:
            api_url = f'http://127.0.0.1:8000/api/v1/movies/{movie_id}/'

        try:
            response = requests.get(api_url, timeout=10) 
            response.raise_for_status() 
            fetched_data = response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching external data: {e}")
        
        context['movie'] = fetched_data
        
        return context


class AdminPageView(TemplateView):
    template_name = "admin.html"


