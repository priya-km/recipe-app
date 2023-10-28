from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin # protecting this view requiring the user to login to view it

# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView): #Add LoginReq here to protect this view
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView): #Loginreq here to protect this view too 
    model = Recipe
    template_name = 'recipes/detail.html'

def home(request):
    return render(request, 'recipes/recipes_home.html')
