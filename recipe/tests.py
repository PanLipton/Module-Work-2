from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category
from django.utils import timezone

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Dessert")
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test Description",
            instructions="Test Instructions",
            ingredients="Test Ingredients",
            category=self.category,
            created_at=timezone.now()
        )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.recipe.title)
