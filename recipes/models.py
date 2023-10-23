from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=350, help_text='Ingredients must be separated by commas.')
    cooking_time = models.FloatField(help_text='Time in minutes.')
    description = models.TextField()
    # pic field add later
    
    # calculate difficulty based on number of ingredients and cooking time, 
    # LEARN TO PROPERLY IMPLEMENT IN A LATER EXERCISE 

    def __str__(self):
        return self.name
