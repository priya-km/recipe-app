from django import forms


CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFF__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard')
)


class RecipeSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(choices=DIFF__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class CreateRecipeForm(forms.Form):
    name = forms.CharField(max_length=120)
    cooking_time = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'In minutes'}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'List ingredients separated by commas'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter recipe description here'}))
    pic = forms.ImageField(required=False)
