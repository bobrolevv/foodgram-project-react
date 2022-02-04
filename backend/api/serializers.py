from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from recipes.models import Ingredient, Recipe, Tag, User


class TagSerializer(serializers.ModelSerializer):
    # name = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Tag
        # fields = ('name',)
        fields = '__all__'


class SpecialUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
        )


class SpecialUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "is_subscribed",
        )


class AuthorRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "is_subscribed",
        )


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = AuthorRecipeSerializer(read_only=True)
    ingredients = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            # 'pub_date',
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



