from rest_framework import serializers
from recipes.models import Ingredient, Recipe, Tag, User


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        # fields = '__all__'
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',

        )

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = (
        #     "email",
        #     "id",
        #     "username",
        #     "first_name",
        #     "last_name",
            # "is_subscribed",
        # )
