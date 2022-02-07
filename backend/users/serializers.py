from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from recipes.models import Subsription
from api.serializers import AuthorRecipeSerializer, SpecialUserSerializer


class SubsriptionSerializer(serializers.ModelSerializer):
    user = SpecialUserSerializer(read_only=True)
    author = AuthorRecipeSerializer(read_only=True)

    class Meta:
        model = Subsription
        fields = ('user', 'author')
        # fields = '__all__'