from datetime import datetime
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.conf import settings

import requests

host = settings.API_SERVICE_URL

def api_get_token(request, url):
    headers = {}
    access = request.COOKIES.get("access")
    if access:
        headers["Authorization"] = f"Bearer {access}"
    return requests.get(url, headers=headers, timeout=10)

def api_patch_token(request, url, data):
    headers = {"Content-Type": "application/json"}
    access = request.COOKIES.get("access")

    if access:
        headers["Authorization"] = f"Bearer {access}"

    return requests.patch(url, json=data, headers=headers, timeout=10)


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

        api_url = f"{host}/api/v1/users/token/"

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

    def dispatch(self, request, *args, **kwargs):
        if not request.COOKIES.get("access"):
            return redirect("login-page")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_url = f"{host}/api/v1/users/me/"

        try:
            response = api_get_token(self.request, api_url)
            response.raise_for_status()
            context["profile"] = response.json()["profile"]
        except Exception as e:
            print("Profile fetch error:", e)
            context["profile"] = None

        return context

    def post(self, request):
        api_url = f"{host}/api/v1/users/me/"
        data = {}

        # Profile fields (only send what changed)
        if request.POST.get("username"):
            data["username"] = request.POST.get("username")

        if request.POST.get("email"):
            data["email"] = request.POST.get("email")

        if request.POST.get("bio"):
            data["bio"] = request.POST.get("bio")

        # Password change (optional)
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")

        if old_password and new_password:
            data["old_password"] = old_password
            data["password"] = new_password

        if not data:
            return redirect("profile-page")

        response = api_patch_token(request, api_url, data)

        if response.status_code != 200:
            return render(
                request,
                self.template_name,
                {
                    "profile": self.get_context_data()["profile"],
                    "error": "Update failed",
                },
            )

        return redirect("profile-page")

class SearchPageView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        movie_name = self.request.GET.get('movie-name') 

        if movie_name:
            
            api_url = f"{host}/api/v1/movies/?title={movie_name}"

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
        movie_id = kwargs.get("movie_id")

        if movie_id is None:
            return context

        recs_url = f"{host}/api/v1/movies/{movie_id}/recommendations/"

        try:
            response = api_get_token(self.request, recs_url)
            response.raise_for_status()
            fetched_data = response.json()

            poster_recs = []

            for rec in fetched_data.get("recommendations", []):
                rec_id = rec.get("id")
                if not rec_id:
                    continue

                try:
                    movie_url = f"{host}/api/v1/movies/{rec_id}/"
                    movie_resp = requests.get(movie_url, timeout=10)
                    movie_resp.raise_for_status()
                    movie_data = movie_resp.json()

                    rec["poster_url"] = movie_data.get("poster_url")

                except requests.RequestException as e:
                    print(f"Poster fetch failed for movie {rec_id}: {e}")
                    rec["poster_url"] = None

                poster_recs.append(rec)

            fetched_data["recommendations"] = poster_recs
            context["recs"] = fetched_data

        except requests.RequestException as e:
            print(f"Error fetching recommendations: {e}")
            context["recs"] = {"recommendations": []}

        return context


class HistoryPageView(TemplateView):
    template_name = "history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_url = f"{host}/api/v1/movies/recommendationhistory/"

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
            api_url = f"{host}/api/v1/movies/{movie_id}/"

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_url = f"{host}/api/v1/admin/model-versions/"

        try:
            response = api_get_token(self.request, api_url)
            response.raise_for_status()
            versions = response.json()

            # Convert created_at to datetime (for formatting)
            for v in versions:
                v["created_at"] = datetime.fromisoformat(
                    v["created_at"].replace("Z", "+00:00")
                )

            context["model_versions"] = versions

        except Exception as e:
            print(f"Error fetching model versions: {e}")
            context["model_versions"] = []

        return context


