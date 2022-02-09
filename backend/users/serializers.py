from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from recipes.models import Subsription
from api.serializers import AuthorRecipeSerializer
from recipes.models import User


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


# class SpecialUserSerializer(UserSerializer):
#     class Meta:
#         model = User
#         fields = (
#             "email",
#             "id",
#             "username",
#             "first_name",
#             "last_name",
#             "is_subscribed",
#         )


#####
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
######


class SubsriptionSerializer(serializers.ModelSerializer):
    # user = SpecialUserSerializer(read_only=True)
    author = SpecialUserSerializer(read_only=True)

    class Meta:
        model = Subsription
        fields = (
            # 'user',
            'author',
        )


# class FollowSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(
#         queryset=User.objects.all(),
#         slug_field='username',
#         default=serializers.CurrentUserDefault(),
#     )
#     following = serializers.SlugRelatedField(
#         queryset=User.objects.all(),
#         slug_field='username',
#     )
#
#     class Meta:
#         fields = ('user', 'following',)
#         model = Follow
#
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=Follow.objects.all(),
#                 fields=['user', 'following'],
#                 message='подписка уже существует',
#             )
#         ]
#
#     def validate(self, data):
#         if data['user'] == data['following']:
#             raise serializers.ValidationError(
#                 'Нельзя подписаться на себя!')
#         return data