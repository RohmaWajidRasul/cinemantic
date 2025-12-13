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

class AccountPageView(TemplateView):
    template_name = "account.html"

class ChatPageView(TemplateView):
    template_name = "chat.html"

class RecommendationPageView(TemplateView):
    template_name = "recommendation.html"

class MoviePageView(TemplateView):
    template_name = "movie.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        request_params = self.request.GET
        
        title = request_params.get('title', '')
        limit = request_params.get('limit', 50)  
        offset = request_params.get('offset', 0)

        api_params = {
            'limit': limit,
            'offset': offset,
        }

        if(title):
            api_params['title'] = title
        
        api_base_url = 'http://127.0.0.1:8000/api/v1/movies/'

        query_string = urlencode(api_params)
        
        # Construct the API endpoint URL with the received parameters
        api_endpoint_with_params = f"{api_base_url}?{query_string}"
        
        # Pass the full to the template
        context['api_movie_list_url'] = api_endpoint_with_params

        return context

class AdminPageView(TemplateView):
    template_name = "admin.html"


