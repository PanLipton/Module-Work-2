from django.shortcuts import render
from .models import Recipe
from django.utils import timezone

def main(request):
    current_year = timezone.now().year
    recipes = Recipe.objects.filter(created_at__year=current_year)
    return render(request, 'main.html', {'recipes': recipes})
