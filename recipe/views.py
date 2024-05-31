from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.utils import timezone

def main(request):
    current_year = timezone.now().year
    recipes = Recipe.objects.filter(created_at__year=current_year)
    return render(request, 'main.html', {'recipes': recipes})
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})