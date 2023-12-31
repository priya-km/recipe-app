from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin # protecting this view requiring the user to login to view it
from .forms import RecipeSearchForm, CreateRecipeForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart
from django.contrib.auth.decorators import login_required

# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView): #Add LoginReq here to protect this view
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView): #Loginreq here to protect this view too 
    model = Recipe
    template_name = 'recipes/detail.html'

def home(request):
    return render(request, 'recipes/recipes_home.html')

def about_view(request):
    return render(request, 'recipes/about.html')

@login_required
def create_view(request):
    create_form = CreateRecipeForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and create_form.is_valid():
        name = create_form.cleaned_data.get('name')
        cooking_time = create_form.cleaned_data.get('cooking_time')
        ingredients = create_form.cleaned_data.get('ingredients')
        pic = create_form.cleaned_data.get('pic')  # Retrieve the uploaded image
        description = create_form.cleaned_data.get('description')

        recipe = Recipe.objects.create(
            name=name,
            cooking_time=cooking_time,
            ingredients=ingredients,
            description=description,
            pic=pic  # Save the image to the recipe

        )

        return redirect(recipe.get_absolute_url())  # Redirect after saving

    context = {
        'create_form': create_form,
    }

    return render(request, 'recipes/create.html', context)



#define function based view - records()
@login_required
#create an instance of RecipeSearchForm that was created in forms.py
def records(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    recipe_diff = None
    chart = None
    qs = None
    #check if button is clicked 
    if request.method == 'POST':
        #check recipe difficulty and chart type
        recipe_diff = request.POST.get('recipe_diff')
        chart_type = request.POST.get('chart_type')

        if recipe_diff == '#1':
            recipe_diff = 'Easy'
        if recipe_diff == '#2':
            recipe_diff = 'Medium'
        if recipe_diff == '#3':
            recipe_diff = 'Intermediate'
        if recipe_diff == '#4':
            recipe_diff = 'Hard'

        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df,
                              labels=recipe_df['name'].values)

            recipe_df = recipe_df.to_html()
    #pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipe_diff': recipe_diff,
        'chart': chart,
        'qs': qs,
    }
    #load the recipes/search.html page using the data that was just prepared above
    return render(request, 'recipes/search.html', context)