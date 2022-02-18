from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from recipes.models import (Ingredient, IngredientRecipe,
                            Recipe,Tag,
                            Follow, Favorite, Cart)
from users.serializers import SpecialUserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientAmountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit')

    class Meta:
        model = IngredientRecipe
        fields = (
            'id',
            'name',
            'measurement_unit',
            'amount'
        )

class IngredientAmountCreateSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), required=True,
        source='ingredient.id'
    )

    class Meta:
        model = IngredientRecipe
        fields = (
            'id',
            'amount'
        )


class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = SpecialUserSerializer(read_only=True)
    ingredients = IngredientAmountSerializer(
        source='ingredientrecipe_set',
        many=True,
        read_only=True
    )
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time',
        )

    def get_is_favorited(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return Recipe.objects.filter(favorites__user=user,
                                     id=obj.id).exists()

    def get_is_in_shopping_cart(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return Recipe.objects.filter(cart__user=user, id=obj.id).exists()


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = IngredientAmountCreateSerializer(
        source='ingredientrecipe_set',
        many=True
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )
    image = Base64ImageField(required=False)

    class Meta:
        model = Recipe
        fields = (
            'ingredients',
            'tags',
            'image',
            'name',
            'text',
            'cooking_time'
        )

    def create(self, validated_data):
        author = self.context['request'].user
        tags = validated_data.pop('tags')
        ingredients = validated_data.pop('ingredientrecipe_set')
        recipe = Recipe.objects.create(**validated_data, author=author)
        for tag in tags:
            recipe.tags.add(tag)
        for ingredient in ingredients:
            current_ingredient = ingredient['ingredient']['id']
            IngredientRecipe.objects.create(
                ingredient=current_ingredient, recipe=recipe,
                amount=ingredient['amount']
            )
        return recipe

    def update(self, instance, validated_data):
        if 'ingredientrecipe_set' in validated_data:
            instance.ingredients.clear()
            ingredients = validated_data.pop('ingredientrecipe_set')
            for ingredient in ingredients:
                current_ingredient = ingredient['ingredient']['id']
                IngredientRecipe.objects.create(
                    ingredient=current_ingredient, recipe=instance,
                    amount=ingredient['amount']
                )
        if 'tags' in validated_data:
            instance.tags.set(validated_data.get('tags'))
        if 'name' in validated_data:
            instance.name = validated_data.get('name', instance.name)
        if 'text' in validated_data:
            instance.text = validated_data.get('text', instance.text)
        if 'image' in validated_data:
            instance.image = validated_data.get('image', instance.image)
        if 'cooking_time' in validated_data:
            instance.cooking_time = validated_data.get(
                'cooking_time', instance.cooking_time)
        instance.save()
        return instance


class CropRecipeSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')
        read_only_fields = ('id', 'name', 'image', 'cooking_time')


class FollowSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='author.id')
    email = serializers.ReadOnlyField(source='author.email')
    username = serializers.ReadOnlyField(source='author.username')
    first_name = serializers.ReadOnlyField(source='author.first_name')
    last_name = serializers.ReadOnlyField(source='author.last_name')
    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'is_subscribed', 'recipes', 'recipes_count')

    def get_is_subscribed(self, obj):
        return Follow.objects.filter(
            user=obj.user, author=obj.author
        ).exists()

    def get_recipes(self, obj):
        request = self.context.get('request')
        limit = request.GET.get('recipes_limit')
        queryset = Recipe.objects.filter(author=obj.author)
        if limit:
            queryset = queryset[:int(limit)]
        return RecipeSerializer(queryset, many=True).data

    def get_recipes_count(self, obj):
        return Recipe.objects.filter(author=obj.author).count()
