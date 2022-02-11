from django.contrib import admin
from .models import Ingredient, Recipe, IngredientRecipe, Tag, Subsription # AuthorRecipes

class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe)
admin.site.register(Tag, TagAdmin)
admin.site.register(Subsription)
# admin.site.register(AuthorRecipes)
