from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=350, help_text='Ingredients must be separated by commas.')
    cooking_time = models.FloatField(help_text='Time in minutes.')
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 7:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 7:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 7:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 7:
            difficulty = 'Hard'
        return difficulty

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
