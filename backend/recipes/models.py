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


class Tag(models.Model):
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=7, default="#ffffff")
    slug = models.SlugField(max_length=64, unique=True)

    def colored_name(self):
        return format_html('<span style="color: #{};">{}</span>', self.hexcolor, )

    def __str__(self):
        return f'{self.title}'


class Recipe(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название рецепта'
    )
    text = models.TextField()
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления (в минутах)',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
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
        upload_to='img/recipes/',
        verbose_name='Картинка'
    )
    is_favorited = models.ManyToManyField(
        User,
        blank=True,
        related_name='is_favorited'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.name}, t - {self.cooking_time} мин.'


class Subsription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='is_subscribed',
        verbose_name='Подписчик'
    )
    author = models.ManyToManyField(
        User,
        blank=True,
        related_name='author_recipe',
        verbose_name='Автор рецепта'
    )


# class Favorites(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='favorit_recipes',
#         verbose_name='Подписчик'
#     )
#     recipe = models.ManyToManyField(
#         Recipe,
#         blank=True,
#         related_name='author_recipe',
#         verbose_name='Автор рецепта'
#     )


class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name_EN', 'hexcolor', 'colored_name')
