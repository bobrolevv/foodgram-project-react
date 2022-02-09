import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Recipe, User

class Command(BaseCommand):
    help = 'Load ingredient data to DB'

    def handle(self, *args, **options):

        with open('recipes/data/ingredients.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                name, unit = row
                Ingredient.objects.get_or_create(name=name, measurement_unit=unit)
            print(f'add {Ingredient.objects.count()} ingredients')

        for i in range(User.objects.count(), User.objects.count() + 10):
            User.objects.get_or_create(
                username=f'user_{i}',
                first_name=f'first_{i}',
                last_name=f'last_{i}',
                email=f'user_{i}@m.ru',
                password='user123456789',
            )
        print(f'add {i} users')

        author = User.objects.get(id='2')
        for i in range(20):
            Recipe.objects.get_or_create(
                name=f'Простой рецепт{i}',
                text=f'Описание этого рецепта {i}',
                image='/img/recipes/1620120965_28-phonoteka_org-p-obed-fon-42_I8sBQcf.jpg',
                cooking_time=i,
                author=author
            )
        print(f'add {i} recipes')