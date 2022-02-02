from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import User
#
#
# class userProfile(models.Model):
#     email = models.EmailField(
#         max_length=254,)
#
#     username = models.OneToOneField(
#         User,
#         max_length=150,
#         on_delete=models.CASCADE,
#         related_name="profile")
#
#     first_name = models.CharField(
#         max_length=150,
#         )
#
#     last_name = models.CharField(
#         max_length=150,
#         )
#
#
#
#     def __str__(self):
#         return self.user.username

# class User(AbstractUser):
#     email = models.EmailField(max_length=254,)
#     first_name = models.CharField(max_length=150,)
#     last_name = models.CharField(max_length=150,)
#
#     def __str__(self):
#         return f'{self.username} {self.first_name} {self.last_name}'
#
#     class Meta:
#         ordering = ['username']
#     #     verbose_name = 'Пользователь'
#     #     verbose_name_plural = 'Пользователи'
    #
    # @property
    # def is_admin(self):
    #     return (self.role == 'admin' or self.is_superuser or self.is_staff)
    #
    # @property
    # def is_moderator(self):
    #     return self.role == 'moderator'