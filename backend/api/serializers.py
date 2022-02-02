from rest_framework import serializers
from recipes.models import Ingredient, Recipe, Tag, User


class TagSerializer(serializers.ModelSerializer):
    title = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = serializers.StringRelatedField(read_only=True)
    ingredients = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        # fields = '__all__'
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'ingredients',
            'name',
            'image',
            'text',
            'cooking_time',
        )


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "is_subscribed",
        )
