from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer, UserCreateSerializer
from recipes.models import Recipe
from rest_framework import serializers

User = get_user_model()


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


class SubsriptionRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "image",
            "cooking_time",
        )


class UserRecipeSerializer(UserSerializer):
    recipes = SubsriptionRecipeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            # "username",
            "first_name",
            "last_name",
            # "is_subscribed",
            'recipes'
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
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class SubsriptionSerializer(serializers.ModelSerializer):
#     author = UserRecipeSerializer(read_only=True)
#
#     class Meta:
#         model = Subsription
#         # model = User
#
#         # fields = '__all__'
#         fields = (
#             # 'username',
#             'author',
#             # 'is_subscribed',
#             # 'author_recipe',
#         )
