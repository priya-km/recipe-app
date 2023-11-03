from django.urls import path
from .views import home
from .views import RecipeListView, RecipeDetailView, about_view, create_view, records

app_name = 'recipes'

urlpatterns = [
    path('', home,),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', records, name='search'),
    path('about/', about_view, name='about'),
    path('create/', create_view, name='create'),
]