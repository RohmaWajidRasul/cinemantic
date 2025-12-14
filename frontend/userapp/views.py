from datetime import datetime
from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
import requests

def api_get_token(request, url):
    headers = {}
    access = request.COOKIES.get("access")
    if access:
        headers["Authorization"] = f"Bearer {access}"
    return requests.get(url, headers=headers, timeout=10)

# All page views 
class HomePageView(TemplateView):
    template_name = "homepage.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        api_url = "http://127.0.0.1:8000/api/v1/users/token/"

        response = requests.post(
            api_url,
            json={
                "username": username,
                "password": password,
            },
            timeout=10,
        )

        if response.status_code != 200:
            return render(
                request,
                self.template_name,
                {"error": "Invalid username or password"},
            )

        user_data = response.json().get("user")

        
        if user_data and user_data.get("is_superuser"):
            django_response = redirect("admin-page")
        else:
            django_response = redirect("search-page")

        for cookie in response.cookies:
            django_response.set_cookie(
                key=cookie.name,
                value=cookie.value,
                httponly=True,
                samesite="Lax",
            )

        return django_response

class RegisterPageView(TemplateView):
    template_name = "register.html"

class ProfilePageView(TemplateView):
    template_name = "profile.html"

class SearchPageView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        movie_name = self.request.GET.get('movie-name') 

        if movie_name:
            
            api_url = f'http://127.0.0.1:8000/api/v1/movies/?title={movie_name}'

            try:

                response = requests.get(api_url, timeout=10) 
                response.raise_for_status() 
                fetched_data = response.json()
                context['movies'] = fetched_data

            except requests.exceptions.RequestException as e:
                print(f"Error fetching external data: {e}")

        return context

class RecommendationPageView(TemplateView):
    template_name = "recommendation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_id = kwargs.get('movie_id')

        if movie_id is not None:
            api_url = f'http://127.0.0.1:8000/api/v1/movies/{movie_id}/recommendations/'

        try:
            response = api_get_token(self.request, api_url)
            response.raise_for_status() 
            fetched_data = response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching external data: {e}")
        
        context['recs'] = fetched_data
        
        return context

class HistoryPageView(TemplateView):
    template_name = "history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_url = "http://127.0.0.1:8000/api/v1/movies/recommendationhistory/"

        try:
            response = api_get_token(self.request, api_url)
            response.raise_for_status()
            history = response.json()

            for entry in history:
                entry["created_at"] = datetime.fromisoformat(
                    entry["created_at"].replace("Z", "+00:00")
                )

            context["history"] = history


        except requests.exceptions.RequestException as e:
            print(f"Error fetching history: {e}")
            context["history"] = []

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


