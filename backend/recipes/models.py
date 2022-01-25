from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    measurement_unit = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'

class Recipe(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название рецепта'
    )
    description = models.TextField()
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления (в минутах)',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='recipe'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='recipes/images',
        verbose_name='Картинка'
    )

    def __str__(self):
        return f'{self.title}, t - {self.cooking_time} мин.'


class Subsription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribed_to',
        verbose_name='Подписчик'
    )


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()


class Tag(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    hexcolor = models.CharField(max_length=7, default="#ffffff")

    def colored_name(self):
        return format_html('<span style="color: #{};">{}</span>', self.hexcolor, )

    def __str__(self):
        return f'{self.title}'

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name_EN', 'hexcolor', 'colored_name')
