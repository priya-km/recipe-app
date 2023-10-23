from django.test import TestCase
from .models import Recipe
# to access Recipe model

# Create your tests here.
class RecipeTest(TestCase):
    def setUpTestData():
        # set up fake recipe using all attributes
        Recipe.objects.create(name='Tea', ingredients='Tea leaves, Water, Sugar', cooking_time=10, description='test description')

    def test_recipe_name(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)
        # Get name metadata to query
        field_label = recipe._meta.get_field('name').verbose_name
        # Compare value to expected result 
        self.assertEqual(recipe.name, 'Tea')
    
    def test_recipe_ingredients(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('ingredients').verbose_name
        self.assertEqual(recipe.ingredients, 'Tea leaves, Water, Sugar')

    def test_recipe_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('cooking_time').verbose_name
        self.assertEqual(recipe.cooking_time, 10)
    
    def test_recipe_description(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('description').verbose_name
        self.assertEqual(recipe.description, 'test description')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)
    

