from django.shortcuts import render

# Create your views here.

# importing api
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html',)


from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
