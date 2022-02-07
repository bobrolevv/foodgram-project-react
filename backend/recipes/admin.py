from django.contrib import admin
from .models import Ingredient, Recipe, IngredientRecipe, Tag, Subsription

class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )


# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe)
admin.site.register(Tag)
admin.site.register(Subsription)