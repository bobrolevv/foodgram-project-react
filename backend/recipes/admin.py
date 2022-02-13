from django.contrib import admin
from .models import (Favorite, Ingredient, Recipe,
                    IngredientRecipe, Tag, Follow,)


class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name_EN', 'hexcolor', 'colored_name')


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe)
admin.site.register(Tag, TagAdmin)
admin.site.register(Favorite)
admin.site.register(Follow)
